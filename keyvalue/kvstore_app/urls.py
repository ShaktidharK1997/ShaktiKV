from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('insert_key/', views.insert_key),
    path('get_key/', views.get_key),
    path('delete_key/', views.delete_key),
]
