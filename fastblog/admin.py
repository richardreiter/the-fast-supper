from django.contrib import admin
from .models import Post

"""
Many thanks to Matt Rudge and CI's 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""
# add post model to admin panel
admin.site.register(Post)
