from django.db import models


class BaseAdvertising(models.Model):
    views = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=30)


class Ad(BaseAdvertising):
    title = models.IntegerField(max_length=30)
    link = models.URLField()
    img_url = models.URLField()
