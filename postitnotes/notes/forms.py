from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "description", "completed", "author"]

class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "description", "favourite", "author"]


