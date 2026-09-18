from rest_framework import serializers
from .models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=['question' , 'option_a' , 'option_b', 'option_c' , 'option_d' , 'answer' , 'category' , 'different_levels' , 'id']