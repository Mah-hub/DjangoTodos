from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import LoginSerializer, RegisterSerializer
from rest_framework import response, status, permissions
from authentication.models import User
from django.contrib.auth import authenticate
# Create your views here.


class AuthUserAPIView(GenericAPIView):

    permission_classes=(permissions.IsAuthenticated,)

    def get(self,request):
        user=request.user
        serializer = RegisterSerializer(user)
        return response.Response(serializer.data)






class RegisterAPIView(GenericAPIView):
    
    serializer_class = RegisterSerializer

    def post(self,request):

        usernameExist = User.objects.filter(username=request.data.get('username'))
        emailExist =  User.objects.filter(email=request.data.get('email'))

        if usernameExist:
            return response.Response({'error':'Username exist' },status=status.HTTP_409_CONFLICT)
        
        if emailExist:
            return response.Response({'error':'Email exist' },status=status.HTTP_409_CONFLICT)

        serializer  = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)

        user = authenticate(username=email,password=password)

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message' : 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return()