from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from django.conf import settings
from .serializers import RegisterSerializer,UserSerializer,ProfileSerializer,UpdateProfileSerializer
from rest_framework.authtoken.models import Token

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            response = Response({'message': 'Login successful'})
            response.set_cookie(
                key='auth_token',
                value=token.key,
                httponly=True,  # Makes cookie inaccessible to JavaScript
                secure=settings.DEBUG is False,  # Use secure cookies in production
                samesite='Lax'  # Adjust as necessary
            )
            return response
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    print("i am here")
    #permission_classes = [permissions.IsAuthenticated]  THIS IS USED ONLY WHEN WE WANT THE SESSION AUTHENTICATION NOT THE COOKIE AUTHENTICATION

    def get(self, request):
        
        token=request.COOKIES.get("auth_token")
        print(token)
        if not token:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            token_instance = Token.objects.get(key=token)
            user=token_instance.user
            profile = Profile.objects.get(user=user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Token.DoesNotExist:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        


class UpdateProfileView(APIView):
    def get_object(self, user):
        return Profile.objects.get(user=user)
        
    def put(self, request):
        token = request.COOKIES.get("auth_token")
        if not token:
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            token_instance = Token.objects.get(key=token)
            user = token_instance.user
            profile = self.get_object(user)
            
            serializer = UpdateProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Token.DoesNotExist:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)