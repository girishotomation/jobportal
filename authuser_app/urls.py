from django.contrib import admin
from django.urls import path
from authuser_app import views


urlpatterns = [
    path('candidateregister/', views.register_candidate,name='candidate_register'),    
    path('hrregister/', views.register_hr,name='hr_register'),
    path('login/', views.login_user,name='login'),   
    path('logout/', views.logout_user,name='logout'),   
]