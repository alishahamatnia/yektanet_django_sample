from datetime import time, datetime

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView, CreateView

from advertising_management.models import Advertiser, Ad, Seen, Click


class ShowAdView(TemplateView):
    template_name = 'ads.html'

    def get(self, request, *args, **kwargs):
        for advertiser in Advertiser.objects.all():
            for ad in advertiser.ads.all():
                self.create_seen(ad=ad, ip=str(kwargs['ip']))

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = {'advertisers': Advertiser.objects.all()}
        return context

    def create_seen(self, ad, ip):
        seen = Seen(seen_ad=ad, time_showed=datetime.now(), seen_by_ip=ip)
        seen.save()


class RedirectToAdLinkView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'advertiser'

    def get(self, request, *args, **kwargs):
        self.create_click(ad=Ad.objects.get(pk=kwargs['pk']), ip=kwargs['ip'])
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        return ad.link

    def create_click(self, ad, ip):
        click = Click(clicked_on=ad, clicked_by_ip=ip)
        click.save()


class CreateAdView(CreateView):
    model = Ad
    fields = ['title', 'link', 'img_url', 'ad_owner']

    def get_success_url(self):
        return '/advertising_management/ads'

    template_name = 'create_form_template.html'
