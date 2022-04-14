from django.db import models
# import User object
from django.contrib.auth.models import User
# import for featured img
from cloudinary.models import CloudinaryField

"""
Many thanks to Matt Rudge and CI's 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""
# tuple for status 0 as draft, 1 as published
STATUS = ((0, "Draft"), (1, "Published"))


# class of Post inherits from standard Model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # foreign key, one-to-many relationship
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        # order posts on descending order
        ordering = ["-created_on"]

    # magic method returns string representation
    def __str__(self):
        return self.title

    # helper method returns total number of likes from post
    def number_of_likes(self):
        return self.likes.count()
