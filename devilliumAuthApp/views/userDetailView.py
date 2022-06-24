from rest_framework import generics

from devilliumAuthApp.models.user import User
from devilliumAuthApp.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer