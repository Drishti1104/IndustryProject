from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting-page'),
    path('posts', views.AllPostsView.as_view(), name='posts-page'),
    path('posts/<int:pk>', views.SinglePostView.as_view(), name='post-detail-page'), #/posts/my-first-post
    path('create-post', views.CreateBlogPost, name='create-post'),
    # path('read-later', views.ReadLaterView.as_view(), name='read-later'),
]