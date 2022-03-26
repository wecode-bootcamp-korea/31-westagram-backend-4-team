from django.urls import path
from .views import PostingView,CommentView, LikesView

urlpatterns = [
    path("/post", PostingView.as_view()),
    path("/comments", CommentView.as_view()), 
    path("/likes", LikesView.as_view())  
]