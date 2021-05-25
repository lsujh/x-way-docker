from django.db import models


class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("id",)


class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    albumId = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    url = models.URLField()
    thumbnailUrl = models.URLField()
    photo = models.ImageField(upload_to="photos")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("id",)
