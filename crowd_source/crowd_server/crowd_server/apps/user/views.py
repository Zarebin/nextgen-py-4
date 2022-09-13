from cgitb import reset
from lib2to3.pgen2 import token
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from crowd_server.apps.user.models import Profile
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions, generics
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpRequest
from .models import Profile
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework import generics
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
            })
    

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
            })





"""
class LoginView(KnoxLoginView):
    
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            response_data = {'status': 'Failed', 'message': 'Invalid username or password'}
            response = JsonResponse(response_data, status=400)
            return response    
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


        
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                response_data = {'status': 'successful', 'message': f'logged in as {user.username}'}
                response = JsonResponse(response_data, status=200)
                return response
        
        response_data = {'status': 'Failed', 'message': 'Invalid username or password'}
        response = JsonResponse(response_data, status=400)
        return response

        """



"""    

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            response_data = {'status': 'successful', 'message': 'Registration successful'}
            response = JsonResponse(response_data, status=200)
            return response 

        response_data = {'status': 'failed', 'message': 'Registration failed. Invalid information'}
        response = JsonResponse(response_data, status=400)
        return response


class LogoutView(APIView):
    queryset = User.objects.all()

    def get(self, request): 
        logout(request)
        response_data = {'status': 'successful', 'message': 'logged out'}
        response_data = JsonResponse(response_data, status=200)
        return response_data


class StatusView(RetrieveAPIView):
    queryset = User.objects.all()

    def get(self, request: HttpRequest):
        try:
            user = request.user
            response_data = {'username': user.username, 'level': user.profile.level, 'score': user.profile.score, "cookie": request.COOKIES}
            response = JsonResponse(response_data, status=200)
            return response
        except:
            response_data = {'username': "Anonymous user", "cookie": request.COOKIES}
            response = JsonResponse(response_data, status=200)
            return response


class RegisterationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_data = {"user": user, "token": }
        return JsonResponse(response_data)

"""

