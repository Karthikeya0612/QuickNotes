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

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'Django' not in title:
    #         raise ValidationError('We only accept notes about Django!')
    #     return title