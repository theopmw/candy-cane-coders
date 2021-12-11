from django.shortcuts import render

def countdown(request):
    context = {}
    return render(request, 'countdown/countdown.html', context)
