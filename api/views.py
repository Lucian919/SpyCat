from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = []  # Allow unrestricted access