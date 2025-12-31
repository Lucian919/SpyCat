from django.urls import path, include
from .views import CatViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cats', CatViewSet, basename='cat')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
