from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
    #template_name = 'blog/index.html'

# def index(requset):
#    posts = Post.objects.all().order_by('-pk')

#     return render(
#         requset,
#         'blog/index.html',
#         {
#             'posts': posts, 
#         }
#     )  


# def single_post_page(request,pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         "blog/single_post_page.html",
#         {
#             'post': post,
#         }
#     )
# Create your views here.
