# Generated by Django 5.0.4 on 2024-04-14 13:22

import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='company')),
                ('subtitle', models.TextField(max_length=1000)),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('salary_start', models.IntegerField(blank=True, null=True)),
                ('salary_end', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(max_length=15000)),
                ('vacancy', models.IntegerField()),
                ('job_type', models.CharField(choices=[('full_time', 'full_time'), ('part_time', 'part_time'), ('remote', 'remote'), ('freelance', 'freelance')], max_length=10)),
                ('experince', models.IntegerField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_category', to='job.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_company', to='job.company')),
            ],
        ),
    ]