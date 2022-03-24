from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import pro_skills, Location, Nanny

# Create your views here.
def index(request):
    nannies = Nanny.objects.all()[:4]

    return render(request,'index.html',{"nannies":nannies})

def about(request):

    return render(request,'about.html')

def contact(request):

    return render(request,'contact.html')

def nannies(request):
    nannies = Nanny.objects.all()

    return render(request,'nannies.html',{"nannies":nannies})

def profile(request):

    return render(request,'profile.html')



def pricing(request):
    nannies = Nanny.objects.all()

    return render(request,'pricing.html',{"nannies":nannies})

def services(request):

    return render(request,'services.html')

def testimonial(request):

    return render(request,'testimonial.html')
