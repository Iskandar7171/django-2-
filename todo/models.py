from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

class Phone(models.Model):
    name = models.CharField(max_length=99,blank=True,null=True)
    info = models.TextField(blank=True,null=True)
    price = models.CharField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

class Student(models.Model):
    first_name = models.CharField(max_length=99,blank=True,null=True)
    last_name = models.CharField(max_length=99,blank=True,null=True)
    phone_number = models.CharField(max_length=99,unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True,null=True)
    age = models.IntegerField(default=0)
    course = models.CharField(max_length=15,choices=[
        ("1-course","1-course"),
        ("2-course","2-course"),
        ("3-course","3-course"),
        ("4-course","4-course")
    ])
    picture = models.ImageField()
    is_finished = models.BooleanField(default=False)
    birthday = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)