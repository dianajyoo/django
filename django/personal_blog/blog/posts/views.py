from django.shortcuts import render, get_object_or_404
from .models import Post # same as `from . import models` to use `models.Post`

# Create your views here.
def home(request):
  # get and sort all post objects by pub date in descending order
  posts = Post.objects.order_by('-pub_date')

  return render(request, 'posts/home.html', {
    'posts': posts
  })

def post_details(request, post_id):
  # post = Post.objects.get(pk=post_id)
  post = get_object_or_404(Post, pk=post_id) # return 404 error page if post object is not found

  return render(request, 'posts/post_detail.html', {
    'post': post
  })

