from django.urls import path
from . import views

app_name = 'scanner'

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('openai/', views.openai_integration, name='openai_integration'),
]
