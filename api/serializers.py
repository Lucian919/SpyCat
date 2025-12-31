from rest_framework import serializers
from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ['name', 'experience_years', 'breed', 'salary', 'created_at', 'updated_at']