from django.db import models

from projects.models import Tag


class Resume(models.Model):
    file = models.FileField(upload_to="resume/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"Resume ({self.uploaded_at:%Y-%m-%d})"


class HeroContent(models.Model):
    portrait = models.ImageField(upload_to="hero/", blank=True, null=True)
    greeting = models.CharField(max_length=100)
    line_one = models.CharField(max_length=60)
    line_two = models.CharField(max_length=60)
    name_first = models.CharField(max_length=40)
    name_last = models.CharField(max_length=40)
    line_three = models.CharField(max_length=60)
    roles = models.CharField(max_length=150)
    meta_line_one = models.CharField(max_length=150, blank=True)
    meta_line_two = models.CharField(max_length=150, blank=True)
    meta_line_three = models.CharField(max_length=150, blank=True)
    year = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"Hero content (updated {self.updated_at:%Y-%m-%d})"


class Quote(models.Model):
    statement = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"Quote (updated {self.updated_at:%Y-%m-%d})"


class AboutSnapshot(models.Model):
    eyebrow = models.CharField(max_length=100)
    headline_one = models.CharField(max_length=60)
    headline_two = models.CharField(max_length=60)
    headline_three = models.CharField(max_length=60)
    headline_sub = models.CharField(max_length=300)
    paragraph = models.TextField()
    currently_label = models.CharField(max_length=40)
    currently_building = models.CharField(max_length=150)
    currently_learning = models.CharField(max_length=150)
    currently_writing = models.CharField(max_length=150)
    currently_exploring = models.CharField(max_length=150)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"About snapshot (updated {self.updated_at:%Y-%m-%d})"


class About(models.Model):
    eyebrow = models.CharField(max_length=100)
    title_line_one = models.CharField(max_length=60)
    title_line_two = models.CharField(max_length=60)
    lede = models.CharField(max_length=300)
    background_heading = models.CharField(max_length=100)
    background_paragraph = models.TextField()
    care_heading = models.CharField(max_length=100)
    care_paragraph = models.TextField()
    philosophy_eyebrow = models.CharField(max_length=100)
    philosophy_quote = models.TextField()
    skills_eyebrow = models.CharField(max_length=100)
    languages_label = models.CharField(max_length=100)
    languages = models.ManyToManyField(Tag, related_name="about_languages")
    frameworks_label = models.CharField(max_length=100)
    frameworks = models.ManyToManyField(Tag, related_name="about_frameworks")
    learning_label = models.CharField(max_length=100)
    learning = models.ManyToManyField(Tag, related_name="about_learning")
    going_eyebrow = models.CharField(max_length=100)
    going_paragraph = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"About page (updated {self.updated_at:%Y-%m-%d})"


class ContactEmail(models.Model):
    email = models.EmailField()
    github_display = models.CharField(max_length=150)
    linkedin_display = models.CharField(max_length=150)
    available_for_label = models.CharField(max_length=100)
    available_for = models.CharField(max_length=150)
    stack_label = models.CharField(max_length=100)
    stack = models.CharField(max_length=150)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"Contact email (updated {self.updated_at:%Y-%m-%d})"


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.name} — {self.submitted_at:%Y-%m-%d}"


class HireRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_type = models.CharField(max_length=120)
    details = models.TextField()
    budget = models.CharField(max_length=60, blank=True)
    timeline = models.CharField(max_length=60, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.name} — {self.project_type}"
