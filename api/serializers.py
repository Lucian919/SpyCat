from rest_framework import serializers
from .models import Cat, Mission, Target, Country
import requests


class CatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cat
        fields = ['id','name', 'experience_years', 'breed', 'salary']

    def validate_breed(self, value):
        response = requests.get("https://api.thecatapi.com/v1/breeds")
        if response.status_code == 200:
            breeds = [breed['name'] for breed in response.json()]
            if value not in breeds:
                raise serializers.ValidationError("Invalid breed. Please provide a valid breed.")
        else:
            raise serializers.ValidationError("Unable to validate breed at this time.")
        return value


class TargetSerializer(serializers.ModelSerializer):
    country = serializers.CharField(write_only=True)  # Accept country name as text
    
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_completed']
        read_only_fields = ['is_completed']
    
    def create(self, validated_data):
        """On create, look up or create Country by name, then create Target."""
        country_name = validated_data.pop('country')
        country, created = Country.objects.get_or_create(name=country_name.strip().lower().capitalize())
        validated_data['country'] = country
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        """On update, handle country lookup/creation if provided."""
        if 'country' in validated_data:
            country_name = validated_data.pop('country')
            country, created = Country.objects.get_or_create(name__iexact=country_name.strip().lower().capitalize())
            validated_data['country'] = country
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        """Customize representation to show country name instead of object."""
        representation = super().to_representation(instance)
        representation['country'] = instance.country.name
        return representation


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True, read_only=True)
    cat = CatSerializer(read_only=True)
    class Meta:
        model = Mission
        fields = ['id','cat', 'targets', 'is_completed']
        read_only_fields = ['is_completed']
