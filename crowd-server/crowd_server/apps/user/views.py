from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework import permissions
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse


class LoginView(APIView):
    
    queryset = User.objects.all()
    #TODO serializer (swagger)

    def post(self, request):
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


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    #TODO serializer

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            response_data = {'status': 'successful', 'message': 'Registration successful'}
            response = JsonResponse(response_data, status=200)
            return response 

        response_data = {'status': 'failed', 'message': 'Registration failed. Invalid information'}
        response = JsonResponse(response_data, status=400)
        return response


class LogoutView(APIView):
    queryset = User.objects.all()
    #TODO serializer

    def get(self, request): 
        logout(request)
        response_data = {'status': 'successful', 'message': 'logged out'}
        response_data = JsonResponse(response_data, status=200)
        return response_data


class StatusView(RetrieveAPIView):
    queryset = User.objects.all()
    #TODO serializer

    def get(self, request):
        # just for test
        username = request.user.username
        response_data = {'username': username}
        response = JsonResponse(response_data, status=200)
        return response



