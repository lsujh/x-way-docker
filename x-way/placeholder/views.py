from django.views.generic import ListView

from .models import Album, Photo


class AlbumView(ListView):
    model = Album
    queryset = Album.objects.all()
    template_name = "albums_list.html"


class PhotosAlbumViews(ListView):
    model = Photo
    queryset = Photo.objects.all()
    template_name = "photos_album_list.html"

    def get_queryset(self):
        photos = self.queryset.filter(
            albumId=self.kwargs.get("pk"),
        )
        return photos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["album"] = Album.objects.filter(id=self.kwargs.get("pk")).first().title
        return context
