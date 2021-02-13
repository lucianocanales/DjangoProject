from django.forms import ModelForm
from django.forms import PasswordInput
from django.contrib.auth.models import User


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update(
            {'autofocus': True, 'placeholder': 'Usuario'})
        self.fields['password'].widget.attrs.update(
            {'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'is_active']
        widgets = {
            'password': PasswordInput()
        }
