from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'abc@site.com'}),
            'url': forms.TextInput(attrs={'placeholder': 'self web-site'}),
        }

