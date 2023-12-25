from django.contrib import admin
from django.urls import path
from hr_app import views


urlpatterns = [
    path('hrdashboard/', views.hrHome_view,name='home'),
    path('postjob/', views.post_new_job_view,name='post_job'),
    path('candidates/', views.candidates_view,name='candidates'),
    path('selectedcandidates/', views.selected_candidates_view,name='selected_candidates'),
]
