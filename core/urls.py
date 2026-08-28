from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('hire/', views.hire_me, name='hire_me'),
    path('projects/', include('projects.urls')),
    path('blog/', include('projects.blog_urls')),
    path('resume/', views.resume, name='resume'),
    path('github/', views.github, name='github'),
    path('adminhub/', include('adminhub.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
