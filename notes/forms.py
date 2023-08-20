from django import forms
from django.core.exceptions import ValidationError
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'text': forms.Textarea(attrs={'class': 'form-control form-control-sm'}),
        }
        labels = {
            'text': "Write your thoughts"
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('We only accept 20 characters in title')
        return title