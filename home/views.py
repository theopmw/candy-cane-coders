from django.shortcuts import render, redirect, reverse

def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('countdown'))
    context = {}
    return render(request, 'home/index.html', context)
