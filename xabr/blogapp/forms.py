from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from mainapp.models import Post


class BlogUserEditForm(forms.Form):
    class Meta:
        model = Post
        fields = ('category', 'name', 'slug', 'description', 'posts_text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
