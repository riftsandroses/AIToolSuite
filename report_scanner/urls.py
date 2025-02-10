from django.urls import path
from .views import report_list, scanner_insights

app_name = 'report_scanner'

urlpatterns = [
    path('reports/', report_list, name='report_list'),
    path('scanner_insights/<str:yaml_name>/', scanner_insights, name='scanner_insights'),
]
