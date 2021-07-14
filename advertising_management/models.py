from django.db import models


class BaseAdvertising(models.Model):
    pass


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=30)


class Ad(BaseAdvertising):
    ad_owner = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name='ads')
    title = models.CharField(max_length=30)
    link = models.URLField()
    img_url = models.URLField()


class Click(models.Model):
    clicked_on = models.ForeignKey(BaseAdvertising, on_delete=models.CASCADE, related_name='clicks')
    clicked_by_ip = models.CharField(max_length=16)
    time_clicked = models.DateTimeField(auto_now=True)


class Seen(models.Model):
    seen_ad = models.ForeignKey(BaseAdvertising, on_delete=models.CASCADE)
    clicked_by_ip = models.CharField(max_length=16)
    time_clicked = models.DateTimeField(auto_now=True)
