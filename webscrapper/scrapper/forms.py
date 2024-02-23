from django import forms
from .models import ProjectDetail,ContactDetail

class ProjectDetails(forms.ModelForm):
  class Meta:
    model = ProjectDetail
    fields = ["project_name", "url",]
    labels = {'project_name': "ProjectName", "url": "Url"}

class ContactDetails(forms.ModelForm):
  class Meta:
    model= ContactDetail
    fields=["name","email","message"]
    labels={'name':'Name','email':'Email','message':'Message'}