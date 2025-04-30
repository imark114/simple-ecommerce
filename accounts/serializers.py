from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import UserProfile

CustomUser = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'address', 'city', 'state', 'country', 'postal_code')

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'password', 'password2', 'profile')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        
        # The profile is automatically created by the signal
        # We just need to update it if profile data is provided
        if profile_data:
            profile = user.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        
        # Update user fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update profile if provided
        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        
        return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username
        return token 