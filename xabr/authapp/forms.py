from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from .models import XabrUser


class XabrUserLoginForm(AuthenticationForm):
    class Meta:
        model = XabrUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class XabrUserRegisterForm(UserCreationForm):
    class Meta:
        model = XabrUser
        fields = ('username', 'first_name', 'password1', 'password2', 'aboutMe', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class XabrUserEditForm(UserChangeForm):
    class Meta:
        model = XabrUser
        fields = ('username', 'first_name', 'aboutMe', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
