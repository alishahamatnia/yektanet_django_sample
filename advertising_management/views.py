from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView, CreateView

from advertising_management.models import Advertiser, Ad


class ShowAdView(TemplateView):
    template_name = 'ads.html'

    def get_context_data(self, **kwargs):
        context = {'advertisers': Advertiser.objects.all()}
        for advertiser in Advertiser.objects.all():
            for ad in advertiser.ads.all():
                ad.inc_views()
                advertiser.inc_views()
        return context


class RedirectToAdLinkView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'advertiser'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['pk'])
        ad.inc_clicks()
        ad.ad_owner.inc_clicks()
        return ad.link


class CreateAdView(CreateView):
    model = Ad
    fields = ['title', 'link', 'img_url', 'ad_owner']
    def get_success_url(self):
        return '/advertising_management/ads'
    template_name = 'create_form_template.html'

