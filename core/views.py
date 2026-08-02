from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import (
    Profile, SkillCategory, Certification, Project,
    WorkExperience, Testimonial
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


def project_detail(request, slug):
    profile = get_profile()
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.exclude(id=project.id).filter(industry=project.industry)[:3]
    context = {
        'profile': profile,
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'core/project_detail.html', context)


def certifications_view(request):
    profile = get_profile()
    certifications = Certification.objects.all()
    context = {'profile': profile, 'certifications': certifications}
    return render(request, 'core/certifications.html', context)


def case_studies(request):
    profile = get_profile()
    context = {'profile': profile}
    return render(request, 'core/case_studies.html', context)


def contact(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # Try to send an email notification if email backend is configured.
            try:
                send_mail(
                    subject=f"New Portfolio Contact: {contact_message.subject}",
                    message=(
                        f"Name: {contact_message.name}\n"
                        f"Email: {contact_message.email}\n\n"
                        f"{contact_message.message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass

            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()

    context = {'profile': profile, 'form': form}
    return render(request, 'core/contact.html', context)
