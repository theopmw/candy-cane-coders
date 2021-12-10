from django.urls import path
from . import views

urlpatterns = [
    path("", views.wishlists, name="wishlists"),
]
