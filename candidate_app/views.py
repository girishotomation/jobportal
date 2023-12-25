from django.shortcuts import render,redirect
from hr_app.models import CandidateApplication,JobPost
from django.contrib.auth.decorators import login_required
from hr_app.models import Hr
from authuser_app.views import validate_hr_user

# Create your views here.

@login_required
def candidate_dash(request): 
     if validate_hr_user(request):
      return redirect('home')
     else:
      available_jobs = JobPost.objects.all()         
      return render(request,'candidate/candidatedash.html',{'data': available_jobs})

@login_required
def candidate_application(request,pk):
     if validate_hr_user(request):
      return redirect('home')
     else:         
          data_from_db=JobPost.objects.filter(id=pk)
          context = {'data_from_db': data_from_db}           
          if request.method=='POST':
               job=JobPost.objects.get(id=pk)
               year= request.POST.get('year')
               experience= request.POST.get('experience')
               resume= request.FILES.get('resume')
               #print(job+experience)
               candidate_job_application=CandidateApplication(user=request.user,job=job,year_passed_out=year,experience=experience,resume=resume)
               candidate_job_application.save() 
               return redirect('candidate_dashboard')        
     return render(request,'candidate/candidateapplicationform.html',context)

@login_required
def view_applied_jobs(request):
    if validate_hr_user(request):
      return redirect('home')
    else:
     applied_job_data=CandidateApplication.objects.filter(user=request.user)       
     return render(request,'candidate/appliedjobs.html',{'applied_jobs_data': applied_job_data} )
    

