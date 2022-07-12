from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from devilliumAuthApp.serializers.userSerializer import UserSerializer

# Django manages views as controllers

# Django will interpret views as controllers
class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):

        # Object creation(User)
        serializer = UserSerializer(data=request.data)

        # Validates data types
        serializer.is_valid(raise_exception=True)

        # Calls create function to create and save the User
        serializer.save()

        # Creates a tokenData var with user and pw info
        tokenData = {"username":request.data["username"], 
                     "password":request.data["password"]}

        # Creates 2 tokens based on tokenData
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)

        # Validates tokens integrity
        tokenSerializer.is_valid(raise_exception=True)
                
        # Returns both validated tokens and the code HTTP_201_CREATED
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)