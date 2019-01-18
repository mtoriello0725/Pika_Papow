from django.urls import path
from . import views

urlpatterns = [
    path('api/services', views.MemeListCreate.as_view()),
    path('', views.MemeListCreate.as_view())
]