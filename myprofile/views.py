from django.shortcuts import render
from . models import *

# Create your views here.

def home(request):
  context = {}
  return render(request, "myprofile/home.html", context)


def about(request):
  about = About.objects.all()
  context = {

      'about': about
  }
  return render(request, "myprofile/about.html", context)


def work(request):
  projects = Work.objects.all()
  context = {

      'projects': projects
  }
  return render(request, "myprofile/work.html", context)


def contact(request):
  email = request.POST.get('email', False)
  contact_us = Contact()
  contact_us.email = email
  contact_us.save()  
  context = {}
  return render(request, "myprofile/contact.html", context)
