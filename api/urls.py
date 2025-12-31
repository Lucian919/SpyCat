from django.urls import path, include
from .views_cat import CatViewSet
from .views_mission import MissionViewSet
from .views_target import TargetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cats', CatViewSet, basename='cat')
router.register(r'missions', MissionViewSet, basename='mission')
router.register(r'targets', TargetViewSet, basename='target')
app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
