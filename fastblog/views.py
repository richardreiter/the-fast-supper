from django.shortcuts import render
# import generic library
from django.views import generic
# import post model that view will based on
from .models import Post


"""
Many thanks to Matt Rudge and CI's 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""


class PostList(generic.ListView):

    # use Post as its model
    model = Post
    # method to render list of posts, filter by published
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # html file that view will render
    template_name = 'index.html'
    # separate into pages, limit 6 posts
    paginate_by = 6
