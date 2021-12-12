from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('increase_day/', login_required(views.increase_day), name="increase_day"),
    path('set_day_11/', login_required(views.set_day_11), name="set_day_11"),
    path('reset_draw/', login_required(views.reset_draw), name="reset_draw"),
]