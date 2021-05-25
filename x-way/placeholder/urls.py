from django.urls import path


from .views import PhotosAlbumViews, AlbumView

urlpatterns = [
    path("photosAlbum/<int:pk>", PhotosAlbumViews.as_view(), name="photos_album_list"),
    path("", AlbumView.as_view(), name="albums_list"),
]
