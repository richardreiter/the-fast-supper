from . import views
from django.urls import path

"""
Many thanks to Matt Rudge and CI's 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""


urlpatterns = [
    # render this class as a view
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('add_post/new', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/edit/', views.UpdatePost.as_view(), name='update_post'),
    path(
        '<slug:slug>/delete/', views.DeletePost.as_view(), name='delete_post'
        ),
]
