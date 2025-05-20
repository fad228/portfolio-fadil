from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('a-propos/', views.about, name='about'),
    path('competences/', views.skills, name='skills'),
    path('projets/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('cv/', views.cv, name='cv'),
]
