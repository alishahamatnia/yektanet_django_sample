from django.db import models


class BaseAdvertising(models.Model):
    views = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)

    def inc_views(self):
        self.views += 1

    def inc_clicks(self):
        self.clicks += 1


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=30)


class Ad(BaseAdvertising):
    ad_owner = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name='ads')
    title = models.CharField(max_length=30)
    link = models.URLField()
    img_url = models.URLField()
