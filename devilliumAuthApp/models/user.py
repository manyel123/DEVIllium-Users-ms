from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        
        # User creation, based on User model
        user = self.model(username=username)

        # Set a password for the user
        user.set_password(password)

        # Save the user into the db
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """

        # Uses create_user function to create a new user
        user = self.create_user(
            username=username,
            password=password,
        )

        # Set the created User as Admin
        user.is_admin = True

        # Save the superUser into the db
        user.save(using=self._db)
        return user

# User class inherits properties from User generic class, also inherits permissions
class User(AbstractBaseUser, PermissionsMixin):

    # User model attributes
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    name = models.CharField('Name', max_length = 30)
    email = models.EmailField('Email', max_length = 100)

    # Overcharging save function allows to add some_salt as a variable to cifer the password
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN' 
        self.password = make_password(self.password, some_salt)

        # Calling to AbstractBaseUser, saves and send the new password parameter
        super().save(**kwargs)

    # UserManager will be used as object
    objects = UserManager()

    # Set USERNAME_FIELD as username
    USERNAME_FIELD = 'username'