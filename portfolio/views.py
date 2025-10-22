from django.shortcuts import render
from .models import CV

def home(request): return render(request, 'portfolio/home.html')
def about(request): return render(request, 'portfolio/about.html')
def skills(request): return render(request, 'portfolio/skills.html')
def projects(request): return render(request, 'portfolio/projects.html')
def services(request): return render(request, 'portfolio/services.html')
def contact(request): return render(request, 'portfolio/contact.html')

def cv(request):
    cv = CV.objects.first()
    if cv:
        cv_url_absolu = request.build_absolute_uri(cv.fichier.url)
    else:
        cv_url_absolu = None
    return render(request, 'portfolio/cv.html', {'cv': cv, 'cv_url_absolu': cv_url_absolu})

def metsw_btp(request):
    return render(request, 'projects/metsw-btp/index.html')
