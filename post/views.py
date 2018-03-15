from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm
from django.utils.text import slugify
# Create your views here.


def homeview(request):
    postList = Post.objects.all()
    context = {
        'posts': postList
    }
    return render(request, 'index.html', context)


def detailview(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context={
        'post':post
    }
    return render(request, 'detail.html', context)


def createview(request):

    if not request.user.is_authenticated:
        return Http404()


    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.User
        post.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def editview(request, slug):
    if not request.user.is_authenticated:
        return Http404

    post = get_object_or_404(Post, slug=slug)

    form = PostForm(request.POST or None, request.FILES or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def deleteview(request, slug):
    if not request.user.is_authenticated:
        return Http404()

    post = get_object_or_404(Post, slug=slug)

    post.delete()

    return redirect('post:index')


