from django.http import HttpRequest


class GetIPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request: HttpRequest, func, args, kwargs):
        ip = request.META.get('REMOTE_ADDR')

        if not request.path_info.startswith('/admin'):
            kwargs['ip'] = ip
