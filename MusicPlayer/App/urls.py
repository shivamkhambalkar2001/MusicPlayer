from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path("add_song/", views.add_song, name="add_song"),
    path("index/", views.index, name="index"),
    path('delete/<int:song_id>/confirmation/', views.delete_confirmation, name='delete_confirmation'),
    path('delete/<int:song_id>/', views.delete_song, name='delete_song'),
    path('download/<int:song_id>/', views.download_song, name='download_song'),
    path('search/', views.search_songs, name='search_song'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
