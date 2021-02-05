from django import forms
from mainapp.models import Comments


class CommentForm(forms.ModelForm):
    '''форма комментариев к статьям'''
    class Meta:
        model = Comments
        fields = ('text', )