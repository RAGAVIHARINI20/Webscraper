from django.urls import path,re_path
from . import views

urlpatterns = [
    path('scraper/', views.scrape, name='scrape'),
    path('createProject/',views.createProject,name='createProject'),
    path('getFile/',views.exportResult,name='getFile'),
    path('contactUs/',views.contactUs,name='contactUs')


]