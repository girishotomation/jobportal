from django.shortcuts import render,redirect
from hr_app.models import JobPost,CandidateApplication,SelectedCandidates
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def hrHome_view(request):
     jobs_data = JobPost.objects.all()    
     return render(request,'hr/hrdashboard.html',{'data': jobs_data})
@login_required
def post_new_job_view(request):
    msg=None
    
    if request.method =='POST':    
    #user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    
     title=request.POST.get('title')
     city=request.POST.get('city')
     company=request.POST.get('company')
     salary_min=request.POST.get('salary-low')
     salary_max=request.POST.get('salary-max')
     last_date=request.POST.get('date')
     msg ="Job added successfully"
     job_post=JobPost(user=request.user,title=title,city=city,company_name=company,salary_rannge_min=salary_min,salary_rannge_max=salary_max,last_apply_date=last_date)
     job_post.save()     
    return render(request,'hr/postjob.html',{'msg':msg})

@login_required
def candidates_view(request):
    all_candidates_data = CandidateApplication.objects.all()
    all_jobposts_data = JobPost.objects.all()    
    return render(request,'hr/candidates.html',{'all_candidates_data': all_candidates_data,'all_jobposts_data':all_jobposts_data})


def selected_candidates_view(request):
    if request.method == 'POST':
        candidateid = request.POST.get('candidateid')
        jobpostid = request.POST.get('jobpostid') 
        candidate = CandidateApplication.objects.get(id=candidateid) 
        jobpost = JobPost.objects.get(id=jobpostid)
        if SelectedCandidates.objects.filter(candidate=candidate).exists()==False:
           SelectedCandidates(job=jobpost,candidate=candidate).save()            
           selected_candidates_data = SelectedCandidates.objects.all()    
           return render(request,'hr/selectedcandidates.html',{'selected_candi_data': selected_candidates_data})
        return redirect('home')

    
