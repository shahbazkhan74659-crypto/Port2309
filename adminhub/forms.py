from django import forms

from core.models import (
    About,
    AboutSnapshot,
    ContactEmail,
    HeroContent,
    Quote,
    Resume,
    ResumeEducation,
    ResumeExperience,
    ResumePage,
)
from projects.models import Post, Project, ProjectImage

from .widgets import LabeledClearableFileInput


def validate_tag_count(tags, min_count=1, max_count=6):
    count = tags.count() if tags is not None else 0
    if count < min_count:
        raise forms.ValidationError("Select at least 1 tag.")
    if count > max_count:
        raise forms.ValidationError(f"Select at most {max_count} tags (you selected {count}).")
    return tags


class TagPickerFormMixin:
    """Renders every field named in `tag_field_names` as a checkbox chip list."""

    tag_field_names = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.tag_field_names:
            if name in self.fields:
                field = self.fields[name]
                field.widget = forms.CheckboxSelectMultiple()
                # Re-attach the field's queryset-derived choices to the new
                # widget instance — swapping the widget after field
                # construction otherwise leaves it with no choices to render.
                field.widget.choices = field.choices


class ProjectForm(TagPickerFormMixin, forms.ModelForm):
    tag_field_names = ("tags",)
    max_featured = 3

    class Meta:
        model = Project
        fields = [
            "title", "slug", "short_description", "description",
            "category", "role", "year", "status",
            "github_url", "live_url", "order", "featured", "tags",
        ]

    def clean_tags(self):
        return validate_tag_count(self.cleaned_data.get("tags"))

    def clean_featured(self):
        featured = self.cleaned_data.get("featured")
        if featured:
            other_featured = Project.objects.filter(featured=True).exclude(pk=self.instance.pk)
            if other_featured.count() >= self.max_featured:
                raise forms.ValidationError(
                    f"At most {self.max_featured} projects can be Featured. "
                    "Unfeature another project first."
                )
        return featured


class ProjectImageForm(forms.ModelForm):
    # Declared explicitly (not auto-generated) so this field does NOT inherit
    # the model's `default=0` as a form initial value — otherwise Django's
    # formset "skip this empty extra row" check (has_changed()) misfires,
    # since it compares that non-None initial against the blank submitted
    # value and wrongly concludes the untouched extra row was edited.
    order = forms.IntegerField(required=False)

    class Meta:
        model = ProjectImage
        fields = ["image", "caption", "order"]

    def clean_order(self):
        return self.cleaned_data.get("order") or 0


ProjectImageFormSet = forms.inlineformset_factory(
    Project,
    ProjectImage,
    form=ProjectImageForm,
    extra=1,
    can_delete=True,
)


class PostForm(TagPickerFormMixin, forms.ModelForm):
    tag_field_names = ("tags",)

    class Meta:
        model = Post
        fields = ["title", "slug", "short_description", "content", "tags", "published_at"]
        widgets = {"published_at": forms.DateInput(attrs={"type": "date"})}

    def clean_tags(self):
        return validate_tag_count(self.cleaned_data.get("tags"))


class AboutForm(TagPickerFormMixin, forms.ModelForm):
    tag_field_names = ("languages", "frameworks", "learning")

    class Meta:
        model = About
        fields = [
            "eyebrow", "title_line_one", "title_line_two", "lede",
            "background_heading", "background_paragraph",
            "care_heading", "care_paragraph",
            "philosophy_eyebrow", "philosophy_quote",
            "skills_eyebrow",
            "languages_label", "languages",
            "frameworks_label", "frameworks",
            "learning_label", "learning",
            "going_eyebrow", "going_paragraph",
        ]

    def clean_languages(self):
        return validate_tag_count(self.cleaned_data.get("languages"))

    def clean_frameworks(self):
        return validate_tag_count(self.cleaned_data.get("frameworks"))

    def clean_learning(self):
        return validate_tag_count(self.cleaned_data.get("learning"))


class HeroContentForm(forms.ModelForm):
    class Meta:
        model = HeroContent
        fields = [
            "portrait", "greeting", "line_one", "line_two",
            "name_first", "name_last", "line_three", "roles",
            "meta_line_one", "meta_line_two", "meta_line_three",
            "year", "location",
        ]
        widgets = {"portrait": LabeledClearableFileInput(clear_label="Remove Image")}


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["statement"]
        widgets = {"statement": forms.Textarea(attrs={"rows": 3})}


class AboutSnapshotForm(forms.ModelForm):
    class Meta:
        model = AboutSnapshot
        fields = [
            "eyebrow", "headline_one", "headline_two", "headline_three",
            "headline_sub", "paragraph", "currently_label",
            "currently_building", "currently_learning",
            "currently_writing", "currently_exploring",
        ]


class ContactEmailForm(forms.ModelForm):
    class Meta:
        model = ContactEmail
        fields = [
            "email", "github_display", "linkedin_display",
            "available_for_label", "available_for",
            "stack_label", "stack",
        ]


class ResumeFileForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["file"]
        widgets = {"file": LabeledClearableFileInput(clear_label="Remove File")}


class ResumePageForm(TagPickerFormMixin, forms.ModelForm):
    tag_field_names = ("languages", "frameworks", "learning")

    class Meta:
        model = ResumePage
        fields = [
            "intro_sub",
            "languages_label", "languages",
            "frameworks_label", "frameworks",
            "learning_label", "learning",
        ]

    def clean_languages(self):
        return validate_tag_count(self.cleaned_data.get("languages"))

    def clean_frameworks(self):
        return validate_tag_count(self.cleaned_data.get("frameworks"))

    def clean_learning(self):
        return validate_tag_count(self.cleaned_data.get("learning"))


class ResumeExperienceForm(forms.ModelForm):
    class Meta:
        model = ResumeExperience
        fields = ["role", "organization", "period", "description", "order"]


class ResumeEducationForm(forms.ModelForm):
    class Meta:
        model = ResumeEducation
        fields = ["degree", "institution", "period", "description", "order"]
