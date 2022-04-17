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

    # display on admin panel title, slug, status, created_on
    list_display = ('title', 'slug', 'status', 'created_on')
    # search title or content to help find post
    search_fields = ['title', 'content']
    # when entering post title, slug field to be auto generated
    prepopulated_fields = {'slug': ('title',)}
    # box to filter posts by status or creation date
    list_filter = ('status', 'created_on')
    # summernote to use blog content field
    summernote_fields = ('content')
