from django.contrib import admin

from .models import About, AboutSnapshot, ContactEmail, ContactRequest, HeroContent, HireRequest, Quote, Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("__str__", "uploaded_at")
    readonly_fields = ("uploaded_at",)


@admin.register(HeroContent)
class HeroContentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "greeting", "updated_at")
    readonly_fields = ("updated_at",)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("__str__", "statement", "updated_at")
    readonly_fields = ("updated_at",)


@admin.register(AboutSnapshot)
class AboutSnapshotAdmin(admin.ModelAdmin):
    list_display = ("__str__", "eyebrow", "updated_at")
    readonly_fields = ("updated_at",)


@admin.register(ContactEmail)
class ContactEmailAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "github_display", "linkedin_display", "available_for", "stack", "updated_at")
    readonly_fields = ("updated_at",)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("__str__", "eyebrow", "updated_at")
    readonly_fields = ("updated_at",)


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submitted_at")
    readonly_fields = ("submitted_at",)


@admin.register(HireRequest)
class HireRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "project_type", "submitted_at")
    readonly_fields = ("submitted_at",)
