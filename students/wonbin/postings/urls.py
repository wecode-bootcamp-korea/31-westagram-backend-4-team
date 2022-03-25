from django.urls import path
from .views import PostingView,CommentView

urlpatterns = [
    path("/post", PostingView.as_view()),
    path("/comments", CommentView.as_view()),   
]