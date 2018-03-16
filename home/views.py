from django.shortcuts import render, redirect, reverse

# Create your views here.


def homeview(request):
    query = request.GET.get('q')
    if query:
        return redirect(reverse('post:index')+ '?q={}'.format(query))
    return render(request, 'home.html', context={'name': 'Beginner'})

