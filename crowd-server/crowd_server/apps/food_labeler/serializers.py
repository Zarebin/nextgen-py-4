from rest_framework import serializers
from .models import Question, QuestionUser


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('image_link', 'question_text')


class QuestionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionUser
        fields = ('user', 'question', 'answer')
