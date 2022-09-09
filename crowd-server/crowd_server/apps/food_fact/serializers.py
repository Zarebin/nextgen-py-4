from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Question, QuestionUser

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('image_link', 'question_text')


class QuestionUserSerializaer(serializers.ModelSerializer):
    class Meta:
        model = QuestionUser
        fields = ('user', 'question')

        