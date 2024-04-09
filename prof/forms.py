from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location']

        widgets = {
            'user': forms.IntegerField(),
            'location': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Адрес'}),
            'bio': forms.Textarea(attrs={'class': 'form-control w-75', 'placeholder': 'Биография'}),
        }