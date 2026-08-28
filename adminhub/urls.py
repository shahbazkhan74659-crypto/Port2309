from django.urls import path

from .views import about, auth, blog, contact, hire, home
from .views import projects as project_views
from .views import resume

app_name = "adminhub"

urlpatterns = [
    # Auth
    path("login/", auth.hub_login, name="login"),
    path("logout/", auth.hub_logout, name="logout"),

    # Home
    path("", home.hub_home, name="home"),
    path("hero/edit/", home.hero_edit, name="hero_edit"),
    path("hero/delete/", home.hero_delete, name="hero_delete"),
    path("quote/edit/", home.quote_edit, name="quote_edit"),
    path("quote/delete/", home.quote_delete, name="quote_delete"),
    path("about-snapshot/edit/", home.about_snapshot_edit, name="about_snapshot_edit"),
    path("about-snapshot/delete/", home.about_snapshot_delete, name="about_snapshot_delete"),

    # Projects
    path("projects/", project_views.project_list, name="project_list"),
    path("projects/add/", project_views.project_create, name="project_create"),
    path("projects/<slug:slug>/edit/", project_views.project_edit, name="project_edit"),
    path("projects/<slug:slug>/delete/", project_views.project_delete, name="project_delete"),

    # About
    path("about/", about.about_hub, name="about"),
    path("about/edit/", about.about_edit, name="about_edit"),
    path("about/delete/", about.about_delete, name="about_delete"),

    # Contact
    path("contact/", contact.contact_hub, name="contact"),
    path("contact/email/edit/", contact.contact_email_edit, name="contact_email_edit"),
    path("contact/email/delete/", contact.contact_email_delete, name="contact_email_delete"),
    path("contact/submissions/<int:pk>/delete/", contact.contact_request_delete, name="contact_request_delete"),

    # Hire Me
    path("hire/", hire.hire_hub, name="hire"),
    path("hire/submissions/<int:pk>/delete/", hire.hire_request_delete, name="hire_request_delete"),

    # Blog
    path("blog/", blog.post_list, name="post_list"),
    path("blog/add/", blog.post_create, name="post_create"),
    path("blog/<slug:slug>/edit/", blog.post_edit, name="post_edit"),
    path("blog/<slug:slug>/delete/", blog.post_delete, name="post_delete"),

    # Resume
    path("resume/", resume.resume_hub, name="resume"),
    path("resume/file/edit/", resume.resume_file_edit, name="resume_file_edit"),
    path("resume/file/delete/", resume.resume_file_delete, name="resume_file_delete"),
    path("resume/page/edit/", resume.resume_page_edit, name="resume_page_edit"),
    path("resume/page/delete/", resume.resume_page_delete, name="resume_page_delete"),
    path("resume/experience/add/", resume.experience_create, name="experience_create"),
    path("resume/experience/<int:pk>/edit/", resume.experience_edit, name="experience_edit"),
    path("resume/experience/<int:pk>/delete/", resume.experience_delete, name="experience_delete"),
    path("resume/education/add/", resume.education_create, name="education_create"),
    path("resume/education/<int:pk>/edit/", resume.education_edit, name="education_edit"),
    path("resume/education/<int:pk>/delete/", resume.education_delete, name="education_delete"),
]
