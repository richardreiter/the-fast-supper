from django.shortcuts import render, get_object_or_404
# import generic library
from django.views import generic, View
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


"""
Many thanks to Matt Rudge and CI's 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""


class PostDetail(View):

    # retrieve post to display it (each slug is unique)
    def get(self, request, slug, *args, **kwargs):
        # filter only active/published posts
        queryset = Post.objects.filter(status=1)
        # published post with correct slug
        post = get_object_or_404(queryset, slug=slug)
        # get comments from post, filter (ascending) to only show approved
        comments = post.comments.filter(approved=True).order_by('created_on')
        # boolean to check if logged in user liked the post
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # send info to render method
        return render(
            # send request through
            request,
            # supply required template
            "post_detail.html",
            # dictionary to supply context
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
