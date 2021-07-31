from django import forms
from .models import CreatePost


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = CreatePost
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Set post title..'}),
        }
