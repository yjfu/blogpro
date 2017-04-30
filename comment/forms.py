from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'text']

        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'type': 'text', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'type': 'email', 'name': 'email'}),
            #   'text': forms.TextInput(attrs={'id': 'message', 'name': 'message', 'class': 'txt'}),
        }
