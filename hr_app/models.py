from django.db import models


# Create your models here.
from django.contrib.auth.models import User

class Hr(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    staff_status = models.BooleanField(default=False)




class JobPost(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    salary_rannge_min=models.IntegerField(default=0)
    salary_rannge_max=models.IntegerField(default=0)
    applied_count=models.IntegerField(default=0)
    last_apply_date=models.DateField()


    def __str__(self):
        return str(self.title)

OPTIONS_STATUS=(('pending','pending'),('selected','selected'))


class CandidateApplication(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)    
    job = models.ForeignKey(to=JobPost,on_delete=models.CASCADE)
    year_passed_out= models.IntegerField(default=0)
    experience= models.IntegerField(default=0)
    resume=models.FileField(upload_to='resume')
    status=models.CharField(choices=OPTIONS_STATUS,max_length=20,default='pending')

    def save(self, *args, **kwargs):
        # Increment applied_count of the corresponding JobPost
        self.job.applied_count += 1
        self.job.save()

        super().save(*args, **kwargs)


class SelectedCandidates(models.Model):
    job=models.ForeignKey(to=JobPost,on_delete=models.CASCADE)
    candidate= models.OneToOneField(to=CandidateApplication,on_delete=models.CASCADE)

