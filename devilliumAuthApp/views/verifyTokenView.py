from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import TokenVerifySerializer

# Token verification based on UserId
class VerifyTokenView(TokenVerifyView):

    def post(self, request, *args, **kwargs):

        # Saves token to validate into var serializer
        serializer = TokenVerifySerializer(data=request.data)

        # Set tokenBackend ALGORITHM type from backend(SIMPLE_JWT)
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])

        try:
            # Validates token integrity
            serializer.is_valid(raise_exception=True)

            # Decodes the token from the backend
            token_data = tokenBackend.decode(request.data['token'],verify=False)

            # Compares user Id between both tokens
            serializer.validated_data['UserId'] = token_data['user_id']

        # If UserID is not the same on both token an error is raised
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        # If validation is successful returns the token and HTTP_200_OK
        return Response(serializer.validated_data, status=status.HTTP_200_OK)