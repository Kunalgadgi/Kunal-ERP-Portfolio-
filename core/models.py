from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Profile(models.Model):
    """Singleton-style model holding the consultant's core info (Home/About)."""
    full_name = models.CharField(max_length=150)
    title = models.CharField(max_length=200, help_text="e.g. ERPNext Functional Consultant & Implementation Specialist")
    tagline = models.CharField(max_length=250, blank=True, help_text="Short one-liner shown in hero section")
    about = models.TextField(help_text="Detailed about-me / summary paragraph(s)")
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True, help_text="Upload CV/Resume PDF")

    years_experience = models.PositiveIntegerField(default=0)
    projects_completed = models.PositiveIntegerField(default=0)
    clients_served = models.PositiveIntegerField(default=0)
    modules_implemented = models.PositiveIntegerField(default=0)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=150, blank=True)

    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    frappe_forum_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.full_name


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=120, help_text="e.g. Accounts, Stock/Inventory, Selling, Buying, HR & Payroll, Manufacturing")
    proficiency = models.PositiveIntegerField(default=80, help_text="Proficiency percentage (0-100)")
    icon_class = models.CharField(max_length=100, blank=True, help_text="Bootstrap Icon class e.g. 'bi-calculator'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200, default="Frappe / ERPNext")
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=150, blank=True)
    credential_url = models.URLField(blank=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-issue_date']

    def __str__(self):
        return self.title


class Project(models.Model):
    INDUSTRY_CHOICES = [
        ('manufacturing', 'Manufacturing'),
        ('retail', 'Retail'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('services', 'Professional Services'),
        ('trading', 'Trading & Distribution'),
        ('nonprofit', 'Non-Profit / NGO'),
        ('other', 'Other'),
    ]

    PROJECT_TYPE_CHOICES = [
        ('erpnext', 'Frappe/ERPNext'),
        ('wordpress', 'WordPress'),
        ('reactnative', 'React Native'),
        ('webapp', 'Web App'),
        ('other', 'Other'),
    ]

    project_type = models.CharField(
        max_length=20, choices=PROJECT_TYPE_CHOICES, default='erpnext',
        help_text="Category used for the portfolio filter buttons"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    client_name = models.CharField(max_length=150, blank=True, help_text="Leave blank if under NDA")
    industry = models.CharField(max_length=30, choices=INDUSTRY_CHOICES, default='other')
    summary = models.CharField(max_length=300, help_text="Short summary shown on cards")
    description = models.TextField(help_text="Full case study description")
    modules_implemented = models.CharField(max_length=300, help_text="Comma separated e.g. Accounts, Stock, Selling, HR")
    challenge = models.TextField(blank=True, help_text="Business challenge / requirement")
    solution = models.TextField(blank=True, help_text="Solution approach implemented")
    results = models.TextField(blank=True, help_text="Outcome / results achieved")
    duration = models.CharField(max_length=100, blank=True, help_text="e.g. 3 months")
    team_size = models.CharField(max_length=50, blank=True)
    cover_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def modules_list(self):
        return [m.strip() for m in self.modules_implemented.split(',') if m.strip()]


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"


class WorkExperience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=150, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=270, unique=True, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    excerpt = models.CharField(max_length=300)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class Testimonial(models.Model):
    client_name = models.CharField(max_length=150)
    client_designation = models.CharField(max_length=150, blank=True)
    client_company = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5, help_text="1-5 stars")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Testimonial from {self.client_name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
