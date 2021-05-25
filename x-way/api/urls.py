from django.urls import path

from api.views import (
    AlbumsApi,
    PhotosAlbumApi,
    AlbumUpdateApi,
    RegistrationAPIView,
    UserTokenObtainPairView,
)

app_name = "v1"

urlpatterns = [
    path("register", RegistrationAPIView.as_view()),
    path("login", UserTokenObtainPairView.as_view()),
    path("albums", AlbumsApi.as_view()),
    path("photosAlbum/<int:pk>", PhotosAlbumApi.as_view()),
    path("albumUpdate/<int:pk>", AlbumUpdateApi.as_view()),
]
