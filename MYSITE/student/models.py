from django.db import models
from django.utils import timezone

# Create your models here.


class Student(models.Model):
    BRANCH_CHOICES = (
        ('ce', 'CE'), ('eee', 'EEE'), ('mech', 'MECH'), ('cse', 'CSE'), ('it', 'IT')
    )
    f_name = models.CharField(verbose_name='First_Name', blank=False, null=False, max_length=255)
    l_name = models.CharField(verbose_name='Second_Name', blank=False, null=False, max_length=255)
    email = models.EmailField(blank=False, max_length=255)
    gender = models.CharField(verbose_name='Gender', blank=False, max_length=255)
    profile_pic = models.FileField()
    address = models.TextField(blank=False)
    course = models.CharField(choices=BRANCH_CHOICES, max_length=255, default=0)
    session_start_year = models.DateField(default=timezone.now)
    session_end_year = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

