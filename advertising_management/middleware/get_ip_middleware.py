class GetIPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, func, args, kwargs):
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        kwargs['ip'] = ip
