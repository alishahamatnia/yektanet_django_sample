import datetime

from django.db import models


class BaseAdvertising(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    view_count = models.IntegerField(default=1)
    click_count = models.IntegerField(default=0)
    click_per_view = models.FloatField(default=0)


class Advertiser(BaseAdvertising):
    name = models.CharField(max_length=30)


class Ad(BaseAdvertising):
    ad_owner = models.ForeignKey(Advertiser, on_delete=models.CASCADE, related_name='ads')
    title = models.CharField(max_length=30)
    link = models.URLField()
    img_url = models.URLField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Click(models.Model):
    clicked_on = models.ForeignKey(BaseAdvertising, on_delete=models.CASCADE, related_name='clicks',
                                   related_query_name='clicks')
    clicked_by_ip = models.CharField(max_length=16)
    time_clicked = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.clicked_on.click_count += 1
        self.clicked_on.click_per_view = float(self.clicked_on.click_count) / self.clicked_on.view_count
        return super(Click, self).save()


class Seen(models.Model):
    seen_ad = models.ForeignKey(BaseAdvertising, on_delete=models.CASCADE, related_name='ad_views',
                                related_query_name='ad_views')
    seen_by_ip = models.GenericIPAddressField()
    time_showed = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.seen_ad.view_count += 1
        self.seen_ad.click_per_view = float(self.seen_ad.click_count) / self.seen_ad.view_count
        return super(Seen, self).save()
