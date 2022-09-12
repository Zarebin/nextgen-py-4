from rest_framework import serializers
from .models import Question

class FoodCompareSerializer(serializers.ModelSerializer):

    question_id = serializers.IntegerField()
    label = serializers.IntegerField()

    class Meta:
        model = Question
        fields = ('question_id', 'label')
