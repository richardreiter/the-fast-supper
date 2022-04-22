from .models import Comment
from django import forms

"""
Many thanks to Matt Rudge and CI's 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""


# CommentForm class inherits from base form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # use comment model
        fields = ('body',)  # display in body field
