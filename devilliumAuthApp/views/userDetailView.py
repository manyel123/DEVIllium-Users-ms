from rest_framework import generics

from devilliumAuthApp.models.user import User
from devilliumAuthApp.serializers.userSerializer import UserSerializer

# RetrieveAPIView returns an element from the collection 
class UserDetailView(generics.RetrieveAPIView):

    # Brings all objects from User table
    queryset = User.objects.all()

    # Sets the class to serialize
    serializer_class = UserSerializer

    # No additional validation may allow users to access each other information
    # An additional token validation may be used to prevent this

    