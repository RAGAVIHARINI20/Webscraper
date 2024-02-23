from django.db import models

# Create your models here.
class ProjectDetail(models.Model):
    id=models.AutoField(primary_key=True)
    project_name=models.CharField(max_length=255)
    url=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

class ContactDetail(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    message=models.TextField()
    contacted_on = models.DateTimeField(auto_now_add=True)

class ProjectOutputDetail(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=255)
    project_name=models.CharField(max_length=255)
    url = models.TextField()
    project_output=models.JSONField()


