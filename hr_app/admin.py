from django.contrib import admin
from hr_app import models

# Register your models here.
@admin.register(models.Hr)
class HrAdmin(admin.ModelAdmin):
    list_display=('id','user')


@admin.register(models.JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display=('id','user','title','city','company_name','salary_rannge_min','salary_rannge_max','applied_count','last_apply_date')    

@admin.register(models.CandidateApplication)
class CandidateApplicationAdmin(admin.ModelAdmin):
    list_display=('id','user','job','year_passed_out','experience','resume','status') 


@admin.register(models.SelectedCandidates)
class SelectedCandidatesAdmin(admin.ModelAdmin):
    list_display=('id','job','candidate')


