from django.db import models
from django.contrib.auth.models import User
from hr_app.models import CandidateApplication,JobPost

# Create your models here.
class MyJobList(models.Model):
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)
    job=models.ForeignKey(to=CandidateApplication, on_delete=models.CASCADE)
    applied_date = models.DateField(auto_now_add=True)


class IsSortList(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    job=models.OneToOneField(to=JobPost,on_delete=models.CASCADE)
    applied_date = models.DateField(auto_now_add=True)