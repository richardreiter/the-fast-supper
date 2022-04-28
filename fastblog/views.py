# reverse to allow look at the url according to urls.py
from django.shortcuts import render, get_object_or_404, reverse
# import generic library
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
# import post model that view will based on
from .models import Post
from .forms import CommentForm
from django.urls import reverse_lazy


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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # get data from form and assign it
        comment_form = CommentForm(data=request.POST)
        # if form valid/all fields completed
        if comment_form.is_valid():
            # set email automatically from user logged in
            comment_form.instance.email = request.user.email
            # set username automatically from user logged in
            comment_form.instance.name = request.user.username
            # call save method
            comment = comment_form.save(commit=False)
            # assign post to it
            comment.post = post
            # save to db
            comment.save()
        # if form not valid return empty comment form instance
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


"""
Many thanks to Matt Rudge and CI's 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        # get relevant post
        post = get_object_or_404(Post, slug=slug)
        # toggle the state, check if post is already liked
        if post.likes.filter(id=request.user.id).exists():
            # if it is already liked, remove the like
            post.likes.remove(request.user)
        # if it hasn't been liked, add like
        else:
            post.likes.add(request.user)

        # reload template/page to see results
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


"""
Many thanks to John Elder's 'Create A Simple Blog With Python
and Django' project - a great reference, inspiration and example:
https://www.youtube.com/watch?v=J7xaESAddDQ
"""


class UpdatePost(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'content', 'excerpt']
    # redirect to home page
    success_url = reverse_lazy('home')


"""
Many thanks to John Elder's 'Create A Simple Blog With Python
and Django' project - a great reference, inspiration and example:
https://www.youtube.com/watch?v=J7xaESAddDQ
"""


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    # redirect to home page
    success_url = reverse_lazy('home')


"""
Many thanks to John Elder's 'Create A Simple Blog With Python
and Django' project - a great reference, inspiration and example:
https://www.youtube.com/watch?v=m3efqF9abyg
"""


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = [
        'title',
        'slug',
        'author',
        'featured_image',
        'excerpt',
        'content',
        'status'
        ]
    # redirect to home page
    success_url = reverse_lazy('home')
