from django.contrib import admin
from candidate_app import models
# Register your models here.

@admin.register(models.MyJobList)
class AppliedJobList(admin.ModelAdmin):
    list_display=('id','user','job','applied_date')

@admin.register(models.IsSortList)
class AppliedJobList(admin.ModelAdmin):
    list_display=('id','user','job','applied_date')

