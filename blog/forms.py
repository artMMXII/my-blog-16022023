from django import forms
from .models import Note

class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 5})
        }
