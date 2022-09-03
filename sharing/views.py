from django.views.generic import ListView, DetailView
from .models import Post, Photo, Tag

# Create your views here.
class PostList(ListView) :
  model = Post
  ordering = '-pk'

class PostDetail(DetailView) :
  model = Post

def tag_page(request, slug) :
  tag = Tag.objects.get(slug=slug)
  post_list = tag.post_set.all()

  return render(
    request,
    'sharing/post_list.html',
    {
      'post_list': post_list,
      'tag': tag,
    }
  )