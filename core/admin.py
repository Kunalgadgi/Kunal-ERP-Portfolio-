from django.contrib import admin
from .models import (
    Profile, SkillCategory, Skill, Certification, Project, ProjectImage,
    WorkExperience, BlogCategory, BlogPost, Testimonial, ContactMessage
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email', 'updated_at')

    def has_add_permission(self, request):
        # Keep it singleton-like: only allow one Profile entry
        return Profile.objects.count() == 0


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'order')
    list_filter = ('category',)
    list_editable = ('proficiency', 'order')


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'issue_date', 'expiry_date', 'order')
    list_editable = ('order',)
    ordering = ('order', '-issue_date')


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'industry', 'client_name', 'is_featured', 'order', 'created_at')
    list_filter = ('project_type', 'industry', 'is_featured')
    list_editable = ('is_featured', 'order')
    search_fields = ('title', 'client_name', 'modules_implemented')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'project_type', 'client_name', 'industry', 'summary', 'cover_image')
        }),
        ('Case Study Details', {
            'fields': ('description', 'challenge', 'solution', 'results', 'modules_implemented')
        }),
        ('Meta', {
            'fields': ('duration', 'team_size', 'project_url', 'is_featured', 'order')
        }),
    )


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'start_date', 'end_date', 'is_current', 'order')
    list_editable = ('order',)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'published_at')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company', 'rating', 'order')
    list_editable = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'is_read')
    list_filter = ('is_read',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'submitted_at')

    def has_add_permission(self, request):
        return False
