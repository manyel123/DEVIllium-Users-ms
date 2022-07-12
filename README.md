# DEVIllium-Users-ms
Microservice for user login and registration into DEVIllium website.

This service was created using Django Rest Framework.
This service allows the creation of an user with parameters as follow:
Username - as a nickname used for login,
Password - as a password used for login,
Name - as user real name,
Email - as user email direction.

Once created, users can login with their username and password. User information will be saved into a database wich must be configured at 'settings.py'.
The service offers:
Login option,
Token refresh option,
User creation option,
User information view,
Token verification option.
