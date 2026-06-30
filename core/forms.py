from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile, HazardReport


def _style_fields(form):
    """Ensure every field has a predictable id (CSS targets .field input/select/textarea by element)."""
    for name, field in form.fields.items():
        field.widget.attrs.setdefault('id', f'id_{name}')


class StyledFormMixin:
    """Mixin that auto-styles fields on init; concrete forms still set their own widgets/attrs as needed."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        _style_fields(self)


class SignUpForm(StyledFormMixin, UserCreationForm):
    """Extended registration form: standard Django auth fields + profile fields."""
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False, label="Phone Number")
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, initial='driver')
    city = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.phone_number = self.cleaned_data.get('phone_number', '')
            profile.role = self.cleaned_data.get('role', 'driver')
            profile.city = self.cleaned_data.get('city', '')
            profile.save()
        return user


class StyledAuthenticationForm(StyledFormMixin, AuthenticationForm):
    """Login form with consistent styling applied."""
    pass


class ProfileUpdateForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'role', 'city']


class UserUpdateForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class HazardReportForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = HazardReport
        fields = ['hazard_type', 'location', 'description', 'severity', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe what you saw — be as specific as possible.'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. NH-16, near City Mall, Bhubaneswar'}),
        }
