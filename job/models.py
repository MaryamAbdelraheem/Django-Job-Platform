from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
class Job(models.Model):
    title = models.CharField(max_length=120)
    location = CountryField()
    create_at = models.DateTimeField( default=timezone.now)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name ='job_company')

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company')
    subtitle = models.TextField(max_length=1000)
    website = models.URLField()
    email = models.EmailField()

class Category(models.Model):
    pass