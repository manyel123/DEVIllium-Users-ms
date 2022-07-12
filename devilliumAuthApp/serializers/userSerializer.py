from rest_framework import serializers
from devilliumAuthApp.models.user import User

# For relational databases linked to the User overcharge 
# functions create and to_representation

# Non relational User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Model to use in this serializer; needs an import from models
        model = User

        # Fields to use from the database
        fields = ['id', 'username', 'password', 'name', 'email']