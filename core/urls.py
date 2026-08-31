from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('projects/', views.project_list, name='project_list'),
    path('case-studies/', views.case_studies, name='case_studies'),
    path('contact/', views.contact, name='contact'),
    path('blog/',views.blog, name='blog'),
]
