from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home-page"),
    path("details/<int:pk>/", views.details, name="details"),
    path("add_review/<int:pk>/", views.add_review, name="add-review"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)