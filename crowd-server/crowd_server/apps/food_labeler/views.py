from django.shortcuts import render
from .models import Question, QuestionUser
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView 
from . import constants
from .utils import update_scores 

class PopulateQuestion(CreateAPIView):

    def get(self, request):
        question_template = 'Is {food} the dish shown in the image?'

        with open('/home/milad/workspace/django/projects/nextgen-py-4/crowd-server/food.txt', 'r') as f:
            for food in f:
                question_text = question_template.format(food=food)
                question = Question(question_text=question_text)
                question.save()

        return JsonResponse({'detail': 'Successfuly populated database'})


class FoodLabeler(APIView):
    
    permission_classes = [permissions.IsAuthenticated] 

    def get(self, request):
        pass


    def post(self, request):
        try:
            question_id = request.POST.get('question_id')
            answer = request.POST.get('label')  
            question = Question.objects.get(pk=question_id)
            user = request.user
            QuestionUser.objects.create(question, user, answer)
            
            if answer == constants.NO:
                question.no_count += 1
                question.count += 1
            elif answer == constants.YES:
                question.yes_count += 1
                question.count += 1
            elif answer == constants.NOT_SURE:
                question.not_sure_count += 1

            if question.count >= constants.SCORE_THRESHOLD:
                question.final_answer = constants.YES if question.yes_count > question.no_count else constants.NO
                awarded_question_users = QuestionUser.objects.filter(question=question, answer=question.final_answer)
                awarded_users = [question_user.user for question_user in awarded_question_users]
                map(update_scores, awarded_users)

            question.save()

            response_data = {}
            response = JsonResponse(response_data, status=201)
            return response_data
                     

        except:
            response_data = {'status': 'failed', 'message': 'Something went wrong'}
            response = JsonResponse(response_data, status=400)
            return response

