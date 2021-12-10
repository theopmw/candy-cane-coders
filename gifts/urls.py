from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('send/', login_required(views.gift_send), name='gift_send'),
    path('receive/', login_required(views.gift_receive), name='gift_receive'),
]