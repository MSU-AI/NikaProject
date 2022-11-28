from django.urls import path
from . import views

app_name = "index"
urlpatterns = [
    path("", views.blank, name="blank"),
    path("index", views.index, name="index"),
    path("decrypt", views.decrypt, name="decrypt"),
]