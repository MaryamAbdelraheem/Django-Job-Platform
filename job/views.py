from django.shortcuts import render
from .models import Job

def job_list(request):
    all_jobs = Job.objects.all()
    return render(request, 'job/job_list.html', {'jobs': all_jobs})

 
