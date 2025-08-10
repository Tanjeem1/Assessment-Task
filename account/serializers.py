from rest_framework import serializers
from account.models import User
from django.contrib.auth import authenticate


#creating a serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)
    




#creating a serializer for user login
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        attrs['user'] = user
        return attrs
    



#creating a serializer for getting user information from database
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name']




#creating a serializer for user can change password 
class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        user = self.context['user']
        old_password = attrs.get('old_password')
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect")
        if password != password2:
            raise serializers.ValidationError("New passwords don't match")
        user.set_password(password)
        user.save()
        return attrs

