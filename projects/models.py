from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=200)
    tags = models.CharField(max_length=200, help_text="Comma-separated, e.g. 'Django, React, Postgres'")
    category = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    year = models.PositiveIntegerField()
    status = models.CharField(max_length=30, help_text="e.g. Active, Shipped, In progress")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["order", "-year"]

    def __str__(self):
        return self.title

    def tag_list(self):
        return [t.strip() for t in self.tags.split(",") if t.strip()]
