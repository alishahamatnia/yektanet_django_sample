from django.shortcuts import render

from django.views import View
from advertising_management.models import Advertiser


class ShowAdView(View):
    template_name = 'ads.html'

    def get(self, request, *args, **kwargs):
        advertisers = Advertiser.objects.all()

        return render(request=request, template_name=self.template_name,
                      context={'advertisers': advertisers})
