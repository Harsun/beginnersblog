from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def homeview(request):
    postList = Post.objects.all()
    query = request.GET.get('q')
    if query:
        postList = postList.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains = query)|
            Q(user__last_name__icontains=query)
        ).distinct()
    paginator = Paginator(postList, 6)

    page = request.GET.get('page')

    posts = paginator.get_page(page)

    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)


def detailview(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment =form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context={
        'post':post,
        'form':form,
    }
    return render(request, 'detail.html', context)


def createview(request):

    if not request.user.is_authenticated:
        return Http404()


    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
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


