from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('report/', views.lab_option, name='lab_option'),  # Default route for the home page
    path('ai_option/', views.ai_option, name='ai_option'),  # Default route for AI Lab Tool option
    path('llm_scanner_report/', views.llm_scanner_report, name='llm_scanner_report'), # Default route for LLM Scanner Report option
]
