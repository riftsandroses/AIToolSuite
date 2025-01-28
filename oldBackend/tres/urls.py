from django.urls import path
from . import views

urlpatterns = [
    path('', views.tres, name='tres'),  # AI Attack Lab page
    path('llmtool/', views.llmtool, name='llmtool'),  # LLM Attack Suite page
]