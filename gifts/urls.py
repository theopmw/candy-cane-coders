from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('given/', login_required(views.gift_given), name='gift_given'),
    path('received/', login_required(views.gift_received), name='gift_received'),
    path('send/<int:gift_id>/<int:user_id>/', login_required(views.gift_send), name='gift_send'),
]