from django.shortcuts import render

def gift_send(request):
    context = {}
    return render(request, 'gifts/gift_send.html', context)

def gift_receive(request):
    context = {}
    return render(request, 'gifts/gift_receive.html', context)