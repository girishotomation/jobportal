from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from hr_app.models import Hr

# Create your views here.

def register_candidate(request):
    messages_registration=None
    if request.method=='POST':
      fname= request.POST.get('fname')
      lname= request.POST.get('lname')
      username= request.POST.get('uname')
      email= request.POST.get('email')
      password= request.POST.get('password')
      confpassword= request.POST.get('confirmpassword')    
      if password != confpassword:
          messages_registration='Passwords did not match'           
          return render(request,'authuser/candidateregistration.html',{'msg':messages_registration})
      if User.objects.filter(username=username).exists():
          messages_registration='User already exists'           
          return render(request,'authuser/candidateregistration.html',{'msg':messages_registration})
      user =User.objects.create_user(username=username,email=email,password=password,first_name=fname,last_name=lname)
      login(request,user)
      return redirect('candidate_dashboard')      
    return render(request,'authuser/candidateregistration.html')




def register_hr(request):
    if request.method=='POST':
         fname= request.POST.get('fname')
         lname= request.POST.get('lname')
         username= request.POST.get('uname')
         email= request.POST.get('email')
         password= request.POST.get('password')
         confpassword= request.POST.get('confirmpassword')  
         if password != confpassword:
            messages_registration='Passwords did not match'           
            return render(request,'authuser/candidateregistration.html',{'msg':messages_registration})
         if User.objects.filter(username=username).exists():
            messages_registration='Username already exists'
            return render(request,'authuser/candidateregistration.html',{'msg':messages_registration})
        # if Hr.objects.filter(user=username).exists():           
         #   messages_registration='HR with this username already exists'
           # return render(request,'authuser/candidateregistration.html',{'msg':messages_registration})
         hruser =User.objects.create_user(username=username,email=email,password=password,first_name=fname,last_name=lname)
         #Hr.objects.create(user=username).save()
         login(request,hruser)  
         return redirect('home')    
    return render(request,'authuser/hrregistration.html')

def login_user(request):
    error_msg=None
    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')    
       user = authenticate(request, username=username, password=password)
       print(user)
       if user is not None:
           login(request,user) 
           if Hr.objects.filter(user=request.user).exists():
            return redirect('home')
           else:   
            return redirect('candidate_dashboard')                      
       else:
           error_msg="Invalid Credentials"
           return render(request,'authuser/login.html',{'error_msg':error_msg})

    return render(request,'authuser/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def validate_hr_user(request):
   if Hr.objects.filter(user=request.user).exists():
      return True
   else:
      return False