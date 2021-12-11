from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('<username>/', login_required(views.profile), name='profile')
]