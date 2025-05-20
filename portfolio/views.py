from django.shortcuts import render
from .models import CV

def home(request): return render(request, 'portfolio/home.html')
def about(request): return render(request, 'portfolio/about.html')
def skills(request): return render(request, 'portfolio/skills.html')
def projects(request): return render(request, 'portfolio/projects.html')
def services(request): return render(request, 'portfolio/services.html')
def contact(request): return render(request, 'portfolio/contact.html')

def cv(request):
    cv = CV.objects.last()  # prend le dernier CV ajouté
    return render(request, 'portfolio/cv.html', {'cv': cv})