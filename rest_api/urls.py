"""All urls available for api requests"""
# rest_api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Routers
router = DefaultRouter()
router.register(r'certification_models', CertificationModelViewSet, basename='certification_model')
router.register(r'periods', PeriodViewSet, basename='period')


urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]