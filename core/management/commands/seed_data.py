import datetime
from django.core.management.base import BaseCommand
from core.models import (
    Profile, SkillCategory, Skill, Certification, Project,
    WorkExperience, BlogCategory, BlogPost, Testimonial
)


class Command(BaseCommand):
    help = "Seed the database with sample ERPNext consultant portfolio data"

    def handle(self, *args, **options):
        if not Profile.objects.exists():
            Profile.objects.create(
                full_name="John Doe",
                title="ERPNext Functional Consultant & Implementation Specialist",
                tagline="Helping SMEs and enterprises implement ERPNext to streamline Accounts, Inventory, Sales, Purchase, HR & Manufacturing operations.",
                about=(
                    "I'm an ERPNext Functional Consultant with hands-on experience leading end-to-end "
                    "ERP implementations for manufacturing, retail, and service-based businesses. "
                    "My focus is on understanding business processes deeply and configuring ERPNext "
                    "(Frappe Framework) to match real-world workflows — from Chart of Accounts setup "
                    "and Stock/Inventory configuration to Sales/Purchase cycles, HR & Payroll, and "
                    "Manufacturing/BOM management.\n\n"
                    "I have delivered multiple successful go-lives, conducted user training sessions, "
                    "and provided post-implementation support to ensure long-term platform adoption."
                ),
                years_experience=5,
                projects_completed=25,
                clients_served=18,
                modules_implemented=40,
                email="john.doe@example.com",
                phone="+91 90000 00000",
                location="Ahmedabad, Gujarat, India",
                linkedin_url="https://linkedin.com/in/johndoe",
                github_url="https://github.com/johndoe",
                frappe_forum_url="https://discuss.frappe.io/u/johndoe",
            )
            self.stdout.write(self.style.SUCCESS("Created Profile"))

        skill_map = {
            "ERPNext Modules": [
                ("Accounts & Finance", 90, "bi-calculator"),
                ("Stock / Inventory", 88, "bi-boxes"),
                ("Selling", 85, "bi-cart-check"),
                ("Buying", 85, "bi-cart-plus"),
                ("HR & Payroll", 80, "bi-people"),
                ("Manufacturing", 75, "bi-gear"),
            ],
            "Consulting Skills": [
                ("Business Process Mapping", 92, "bi-diagram-3"),
                ("Requirement Gathering", 90, "bi-clipboard-check"),
                ("User Training", 88, "bi-mortarboard"),
                ("UAT & Go-Live Support", 85, "bi-rocket-takeoff"),
            ],
            "Technical": [
                ("Custom Print Formats", 80, "bi-file-earmark-text"),
                ("Workflows & Notifications", 78, "bi-diagram-2"),
                ("Reports & Query Reports", 75, "bi-bar-chart"),
                ("Basic Python/Frappe Framework", 65, "bi-code-slash"),
            ],
        }
        for cat_name, skills in skill_map.items():
            category, _ = SkillCategory.objects.get_or_create(name=cat_name)
            for i, (name, prof, icon) in enumerate(skills):
                Skill.objects.get_or_create(
                    category=category, name=name,
                    defaults={'proficiency': prof, 'icon_class': icon, 'order': i}
                )

        if not Certification.objects.exists():
            Certification.objects.create(
                title="ERPNext Certified Implementer",
                issuing_organization="Frappe School",
                issue_date=datetime.date(2023, 6, 1),
                credential_id="ERP-2023-00123",
            )
            Certification.objects.create(
                title="Frappe Framework Fundamentals",
                issuing_organization="Frappe School",
                issue_date=datetime.date(2022, 11, 15),
            )
            self.stdout.write(self.style.SUCCESS("Created sample certifications"))

        if not Project.objects.exists():
            Project.objects.create(
                title="End-to-End ERPNext Implementation for Textile Manufacturer",
                project_type="erpnext",
                industry="manufacturing",
                summary="Implemented Accounts, Stock, Manufacturing & Selling modules for a mid-size textile manufacturer.",
                description=(
                    "Led a full ERPNext rollout for a textile manufacturing company, replacing "
                    "disconnected spreadsheets and legacy software with a unified system."
                ),
                modules_implemented="Accounts, Stock, Manufacturing, Selling, Buying",
                challenge="Client had no centralized system; inventory and production tracking were manual and error-prone.",
                solution="Configured BOM-driven manufacturing, warehouse-wise stock tracking, and automated accounting entries.",
                results="Reduced inventory discrepancies by 80% and cut monthly closing time from 7 days to 2 days.",
                duration="4 months",
                team_size="3 consultants",
                is_featured=True,
            )
            Project.objects.create(
                title="Retail Chain POS & Inventory Rollout",
                project_type="erpnext",
                industry="retail",
                summary="Deployed ERPNext POS across 6 retail outlets with centralized inventory control.",
                description="Implemented ERPNext Point of Sale and Stock modules across multiple retail locations with real-time sync.",
                modules_implemented="POS, Stock, Selling, Accounts",
                challenge="Each outlet used separate billing systems with no centralized visibility.",
                solution="Rolled out ERPNext POS with barcode scanning and centralized warehouse-wise inventory.",
                results="Achieved real-time stock visibility across all outlets and reduced billing errors significantly.",
                duration="2 months",
                team_size="2 consultants",
                is_featured=True,
            )
            Project.objects.create(
                title="Business Website Revamp",
                project_type="wordpress",
                industry="services",
                summary="Professional WordPress business website with custom theme optimization and SEO setup.",
                description="Designed and developed a fast, responsive WordPress website with a custom theme for a services business.",
                modules_implemented="WordPress, Custom Theme, SEO",
                duration="3 weeks",
                team_size="1 developer",
                is_featured=True,
            )
            Project.objects.create(
                title="Field Service Mobile App",
                project_type="reactnative",
                industry="services",
                summary="Cross-platform React Native app for field service staff to log visits and sync with ERPNext.",
                description="Built a React Native mobile app integrated with ERPNext via REST API for field service tracking.",
                modules_implemented="React Native, ERPNext API Integration",
                duration="6 weeks",
                team_size="2 developers",
                is_featured=True,
            )
            self.stdout.write(self.style.SUCCESS("Created sample projects"))

        if not WorkExperience.objects.exists():
            WorkExperience.objects.create(
                company="ERP Solutions Pvt Ltd",
                role="Senior ERPNext Functional Consultant",
                location="Ahmedabad, India",
                start_date=datetime.date(2022, 1, 1),
                is_current=True,
                description="Leading ERPNext implementations for manufacturing and retail clients, managing full project lifecycle from requirement gathering to go-live support.",
                order=0,
            )
            WorkExperience.objects.create(
                company="Tech Consulting Co.",
                role="ERPNext Functional Consultant",
                location="Ahmedabad, India",
                start_date=datetime.date(2019, 6, 1),
                end_date=datetime.date(2021, 12, 31),
                description="Implemented ERPNext for SME clients across various industries, configured accounting and inventory modules.",
                order=1,
            )
            self.stdout.write(self.style.SUCCESS("Created work experience"))

        if not Testimonial.objects.exists():
            Testimonial.objects.create(
                client_name="Rajesh Patel",
                client_designation="Operations Head",
                client_company="Patel Textiles",
                message="The ERPNext implementation transformed how we manage production and inventory. Highly professional and responsive throughout the project.",
                rating=5,
            )
            self.stdout.write(self.style.SUCCESS("Created testimonial"))

        if not BlogCategory.objects.exists():
            cat = BlogCategory.objects.create(name="Implementation Tips")
            BlogPost.objects.create(
                title="5 Tips for a Smooth ERPNext Go-Live",
                category=cat,
                excerpt="Key lessons learned from managing multiple ERPNext go-lives without major disruptions.",
                content="1. Plan UAT thoroughly.\n2. Train users early.\n3. Migrate clean data.\n4. Keep a rollback plan.\n5. Provide hypercare support post go-live.",
            )
            self.stdout.write(self.style.SUCCESS("Created sample blog post"))

        self.stdout.write(self.style.SUCCESS("Seed data complete!"))
