from django.contrib import admin
from .models import Category, Job, Company
# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'company', 'job_type', 'vacancy', 'category']
    search_fields = ('title', 'category', 'location')
    list_filter = ('vacancy', 'job_type', 'category', 'experince')

admin.site.register(Job,JobAdmin)
admin.site.register(Company)
admin.site.register(Category)
 