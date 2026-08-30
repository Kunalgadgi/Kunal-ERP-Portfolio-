from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import (
    Profile, SkillCategory, Certification, Project,
    WorkExperience, Testimonial, BlogPost
)
from .forms import ContactForm


def get_profile():
    return Profile.objects.first()


def home(request):
    profile = get_profile()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    certifications = Certification.objects.all()[:6]
    testimonials = Testimonial.objects.all()
    experiences = WorkExperience.objects.all()

    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'featured_projects': featured_projects,
        'certifications': certifications,
        'testimonials': testimonials,
        'experiences': experiences,
    }
    return render(request, 'core/home.html', context)


def about(request):
    profile = get_profile()
    experiences = WorkExperience.objects.all()
    certifications = Certification.objects.all()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    context = {
        'profile': profile,
        'experiences': experiences,
        'certifications': certifications,
        'skill_categories': skill_categories,
    }
    return render(request, 'core/about.html', context)


def project_list(request):
    profile = get_profile()
    projects = Project.objects.all()

    context = {
        'profile': profile,
        'projects': projects,
        'project_types': Project.PROJECT_TYPE_CHOICES,
    }
    return render(request, 'core/project_list.html', context)


def case_studies(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'core/case_studies.html', context)


def contact(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data without saving to database
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email notification
            try:
                send_mail(
                    subject=f"New Portfolio Contact: {subject}",
                    message=(
                        f"Name: {name}\n"
                        f"Email: {email}\n\n"
                        f"{message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL or email,
                    recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                messages.error(request, f"Failed to send message: {str(e)}")
                return redirect('contact')

            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()

    context = {'profile': profile, 'form': form}
    return render(request, 'core/contact.html', context)


def blog(request):
    profile = get_profile()
    blog_posts = BlogPost.objects.filter(published=True).order_by('-created_at') if BlogPost.objects.exists() else []
    context = {'profile': profile, 'blog_posts': blog_posts}
    return render(request, 'core/blog.html', context)