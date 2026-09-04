from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from projects.models import Post, Project


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return [
            "home",
            "about",
            "contact",
            "hire_me",
            "projects",
            "blog",
            "resume",
            "github",
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return 1.0 if item == "home" else 0.5

    def changefreq(self, item):
        return "weekly" if item == "home" else "monthly"


class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse("project_detail", args=[obj.slug])


class PostSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Post.objects.all()

    def location(self, obj):
        return reverse("blog_detail", args=[obj.slug])

    def lastmod(self, obj):
        return obj.published_at


sitemaps = {
    "static": StaticViewSitemap,
    "projects": ProjectSitemap,
    "blog": PostSitemap,
}
