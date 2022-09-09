from django.shortcuts import render
from .models import Question, QuestionUser
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView 


class PopulateQuestion(CreateAPIView):

    def get(self, request):
        question_template = 'Is {food} the dish shown in the image?'

        with open('/home/milad/workspace/django/projects/nextgen-py-4/crowd-server/food.txt', 'r') as f:
            for food in f:
                question_text = question_template.format(food=food)
                question = Question(question_text=question_text)
                question.save()

        return JsonResponse({'detail': 'Successfuly populated database'})

