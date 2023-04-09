from django.urls import path, include
from rest_framework import routers
from .views import OCRViewSet


router = routers.DefaultRouter()
router.register('',OCRViewSet, basename='ocr')

urlpatterns = [
    path('', include(router.urls)),
]