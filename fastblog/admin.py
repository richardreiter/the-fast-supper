from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

"""
Many thanks to Matt Rudge and CI's 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""


# decorator to register post model and post admin class
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # summernote to use blog content field
    summernote_fields = ('content')
