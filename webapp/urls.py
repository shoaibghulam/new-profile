
from django.urls import path
from .views import *
urlpatterns = [
    path('', Index , name="index"),

    # ------------dashboard urls
    path('login',Login , name="login"),
    path('dashboard', Dashboard , name="dashboard"),
]
