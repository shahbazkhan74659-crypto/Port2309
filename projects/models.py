from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, related_name="projects")
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


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")
    published_at = models.DateField()

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title
