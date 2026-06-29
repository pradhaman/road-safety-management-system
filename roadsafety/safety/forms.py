from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import HazardReport


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-input'})


class HazardReportForm(forms.ModelForm):
    class Meta:
        model = HazardReport
        fields = ['title', 'hazard_type', 'location', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Brief title of the hazard'}),
            'hazard_type': forms.Select(attrs={'class': 'form-input'}),
            'location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. NH-16 near Bhubaneswar Toll'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Describe the hazard in detail...'}),
        }
