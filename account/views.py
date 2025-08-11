from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserChangePasswordSerializer, UserLoginSerializer, UserProfileSerializer, UserRegistrationSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

#abose those all are dependencies used in this file




def get_tokens_for_user(user): #this function is for crating custom token generation
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView): #for user registration process this function will help user to register
    renderer_classes = [UserRenderer]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)  #taking the serializer and requesting data from that
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user) #generating for token creation
            return Response({'token': token, 'msg': 'Registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView): #for user login process this function will help user to login
    renderer_classes = [UserRenderer]
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = get_tokens_for_user(user)
            return Response({'token': token, 'msg': 'Login successful'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserProfileView(APIView): # to see user info from database this function will help 
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)



class UserChangePasswordView(APIView): #user can change password with this function 
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            return Response({'msg': 'Password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

