from django import forms
from .models import CreateCkPost

class CreateCkPostForm(forms.ModelForm):
    class Meta:
        model = CreateCkPost
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'How to learn Dp effectively'}),
        }
