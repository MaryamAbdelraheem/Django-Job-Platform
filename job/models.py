from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.utils.text import slugify

#tuples of tuples ; one stored at databse & one appeare to the user
JOB_TYPE = (
    ('full_time','full_time'),
    ('part_time','part_time'),
    ('remote','remote'),
    ('freelance','freelance'),
)


class Job(models.Model):
    title = models.CharField(max_length=120)
    location = CountryField()
    create_at = models.DateTimeField( default=timezone.now)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name ='job_company')
    salary_start = models.IntegerField(null=True, blank=True)
    salary_end = models.IntegerField(null=True, blank=True )
    description = models.TextField(max_length= 15000)
    vacancy =  models.IntegerField()
    job_type = models.CharField(choices=JOB_TYPE, max_length=10)
    experince = models.IntegerField()
    category = models.ForeignKey('Category', related_name='job_category', on_delete=models.SET_NULL, null=True, blank=True )
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
       self.slug = slugify(self.title) 
       super(Job, self).save(*args, **kwargs) # Call the real save() method

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company')
    subtitle = models.TextField(max_length=1000)
    website = models.URLField()
    email = models.EmailField()
    def __str__(self):
        return self.name 

class Category(models.Model):
    name = models.CharField(max_length=30)
    logo = models.CharField(max_length=30)
    def __str__(self):
        return self.name  