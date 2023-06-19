from django.db import models


class Url(models.Model):
    original_url = models.URLField(max_length=255)
    key = models.CharField(max_length=6)

