from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name="home-page"),
    path("details/<int:pk>/", views.details, name="details"),
    path("add_review/<int:pk>/", views.add_review, name="add-review"),
]