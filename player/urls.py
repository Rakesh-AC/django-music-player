from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.song_list, name="song_list"),
    path("/upload", views.upload_song, name="upload_song"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

