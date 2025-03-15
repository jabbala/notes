from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-5'}),
        }
        labels={
            'content': 'Write your thought here!',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('Title must start with "Django"')
        return title
