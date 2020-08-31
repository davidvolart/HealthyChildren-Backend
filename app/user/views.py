from rest_framework import generics
from user.serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


@api_view(['POST'])
def authenticate_user(request):
    validated_email = request.data.get("email")
    validated_password = request.data.get("password")

    user = authenticate(username=validated_email, password=validated_password)
    if user is not None:
        return Response({"message": "User authenticated"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User doesn't exists"}, status=status.HTTP_404_NOT_FOUND)
