from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","username","email")

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'age', 'weight', 'height', 'fitness_goals','profile_picture')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user)
        return user
    
class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=("age","weight","height","fitness_goals","profile_picture")