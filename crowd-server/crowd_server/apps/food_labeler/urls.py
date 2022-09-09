from django.urls import path
from . import views


urlpatterns = [
    path('populate-questions', views.PopulateQuestion.as_view()),    
    path('', views.FoodLabelerView.as_view()),
]
