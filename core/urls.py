from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('certifications/', views.certifications_view, name='certifications'),
    path('case-studies/', views.case_studies, name='case_studies'),
    path('contact/', views.contact, name='contact'),
]
