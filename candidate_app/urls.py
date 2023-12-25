from django.contrib import admin
from django.urls import path
from candidate_app import views


urlpatterns = [    
    path('candidate-dashboard/', views.candidate_dash,name='candidate_dashboard'),            
    path('candidate-dashboard/<int:pk>', views.candidate_application,name='candidateapplication'), 
    path('candidate-appliedjobs/', views.view_applied_jobs,name='candidateappliedjobs'),
]