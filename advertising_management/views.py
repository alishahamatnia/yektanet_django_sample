from django.views.generic import TemplateView

from advertising_management.models import Advertiser


class ShowAdView(TemplateView):
    template_name = 'ads.html'

    def get_context_data(self, **kwargs):
        context = {'advertisers': Advertiser.objects.all()}
        return context
