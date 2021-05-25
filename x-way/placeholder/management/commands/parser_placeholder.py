import requests
from urllib.parse import urlparse
from PIL import Image

from django.core.management.base import BaseCommand
from django.conf import settings

from placeholder.models import Album, Photo


class Command(BaseCommand):
    help = "Parser placeholder"

    def handle(self, *args, **kwargs):
        url = "http://jsonplaceholder.typicode.com/"
        albums = requests.get(url + "albums")
        if albums.status_code == 200:
            for album in albums.json():
                Album.objects.get_or_create(
                    id=album["id"],
                    defaults={"userId": album["userId"], "title": album["title"]},
                )
        else:
            return albums.status_code

        photos = requests.get(url + "photos")
        if photos.status_code == 200:
            for photo in photos.json():
                file_name = urlparse(photo["url"]).path.split("/")[-1]
                resp = requests.get(
                    f"https://via.placeholder.com/1000/{file_name}", stream=True
                )
                if resp.status_code == 200:
                    resp.raw.decode_content = True
                    with Image.open(resp.raw) as img:
                        image = img.resize((500, 500))
                        photo_url = f"photos/{file_name}.png"
                        image.save(f"{settings.MEDIA_ROOT}/{photo_url}")
                    Photo.objects.get_or_create(
                        id=photo["id"],
                        defaults={
                            "photo": photo_url,
                            "albumId_id": photo["albumId"],
                            "title": photo["title"],
                            "url": photo["url"],
                            "thumbnailUrl": photo["thumbnailUrl"],
                        },
                    )
                else:
                    return resp.status_code
        else:
            return photos.status_code
