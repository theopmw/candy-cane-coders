from django.shortcuts import render
from gifts.models import Gift

def countdown(request):
    gifts = Gift.objects.all()
    context = {'gifts': gifts}
    return render(request, 'countdown/countdown.html', context)
