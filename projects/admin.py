from django import forms
from django.contrib import admin

from .models import Post, Project, ProjectImage, Tag


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

    def clean_tags(self):
        tags = self.cleaned_data.get("tags")
        count = tags.count() if tags is not None else 0
        if count < 1:
            raise forms.ValidationError("Select at least 1 tag.")
        if count > 6:
            raise forms.ValidationError(f"Select at most 6 tags (you selected {count}).")
        return tags


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ("image", "caption", "order")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ("title", "category", "year", "status", "featured", "order")
    list_editable = ("featured", "order")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    inlines = [ProjectImageInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def clean_tags(self):
        tags = self.cleaned_data.get("tags")
        count = tags.count() if tags is not None else 0
        if count < 1:
            raise forms.ValidationError("Select at least 1 tag.")
        if count > 6:
            raise forms.ValidationError(f"Select at most 6 tags (you selected {count}).")
        return tags


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ("title", "published_at")
    filter_horizontal = ("tags",)
    prepopulated_fields = {"slug": ("title",)}
