from django import forms


class LabeledClearableFileInput(forms.ClearableFileInput):
    """Same as Django's default file-with-existing-value widget, but with a
    custom label for the clear control (styled as a button in CSS, see
    `.hub-remove-file` in static_src/css/input.css) instead of the generic
    "Clear" checkbox."""

    def __init__(self, clear_label="Remove", attrs=None):
        self.clear_checkbox_label = clear_label
        super().__init__(attrs)
