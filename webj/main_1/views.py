from django.shortcuts import render
from .models import Post
def data(request):

    return render(request, 'main_1/data.html')

def test(request):
    posts = Post.objects.all()
    return render(request, 'main_1/test.html', {'posts': posts})

