from django.conf import settings
from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class Link(models.Model):
    text = models.CharField(max_length=130, blank=False)
    url = models.URLField(blank=False)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(default=timezone.now)

    # Este tipo de notación en una función de python significa que la función devolverá
    # el tipo de dato indicado en la -> En este caso devuelve una string
    def __str__(self) -> str:
        return f"{self.text} | {self.url}"

class Video(models.Model):
    video = EmbedVideoField(null=True, blank=True)  #lo mismo que URLField()