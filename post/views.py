from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForm
# Create your views here.


def homeview(request):
    postList = Post.objects.all()
    context = {
        'posts': postList
    }
    return render(request, 'index.html', context)


def detailview(request, id):
    post = get_object_or_404(Post, id=id)
    context={
        'post':post
    }
    return render(request, 'detail.html', context)


def createview(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def editview(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def deleteview(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')


