from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


def wtp_list(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'wtp/index.html',
        {
            'posts': posts,
        }
    )


# def wtp_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'wtp/wtp_detail.html',
#         {
#             'post': post,
#         }
#     )
class Depression(ListView):
    model = Post
    template_name = 'wtp/depression.html'


class Gender(ListView):
    model = Post
    template_name = 'wtp/gender.html'


class Fine(ListView):
    model = Post
    template_name = 'wtp/fine.html'


class Good(ListView):
    model = Post
    template_name = 'wtp/good.html'


class Age(ListView):
    model = Post
    template_name = 'wtp/age.html'


class Book(ListView):
    model = Post
    template_name = 'wtp/book.html'
