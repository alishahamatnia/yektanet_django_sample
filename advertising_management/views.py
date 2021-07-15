import json
from datetime import time, datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView, RedirectView, CreateView, DetailView

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


class GetReportView(View):
    def get(self, *args, **kwargs):
        ans = {'ad_click_views': '', 'ad_click_per_view': ''}
        for ad in Ad.objects.all():
            ans['ad_click_views'] += str((self.calculate_ad_views_and_clicks(ad))) + ','
        res = self.order_by_click_per_view()
        for i in res:
            ans['ad_click_per_view'] += str(res)
        ans['              time             '] = self.calculate_average()
        return HttpResponse(content=ans.items())

    def calculate_ad_views_and_clicks(self, ad: Ad):
        return str({'ad': ad.id[0], 'ad_views': ad.view_count, 'ad_clicks': ad.click_count})

    def order_by_click_per_view(self):
        return Ad.objects.all().order_by('-click_per_view')

    def calculate_average(self):
        clicks = Click.objects.all().order_by('-time_clicked')
        views_ = Seen.objects.all().order_by('-time_showed')
        i = j = 0
        pending = True
        ans = 0
        while i != len(clicks):
            if i >= len(clicks) or j >= len(views_):
                break
            if views_[j].time_showed < clicks[i].time_clicked and pending:
                ans += clicks[i].time_clicked.timestamp - views_[j].time_showed.timestamp
                pending = False
            elif not pending:
                i += 1
                pending = 1
            elif j < len(views_):
                j += 1

        return ans
