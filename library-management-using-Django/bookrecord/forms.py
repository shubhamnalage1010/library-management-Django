from django import forms
from .models import Book

class BookRegistration(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.TextInput( attrs={'class':'form-control'})
        }