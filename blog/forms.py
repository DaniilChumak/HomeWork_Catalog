from django import forms
from catalog.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "slug", "content", "preview_image", "is_published"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "preview_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }