from django import forms
from django.forms import Textarea
from mainapp.models import Comments


class CommentForm(forms.ModelForm):
    """форма комментариев к статьям"""

    class Meta:
        model = Comments
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
        self.fields['text'].widget = Textarea(attrs={'rows': 2})
