from statistics.requests_counter import RequestTracker


class RequestStatisticsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.page_view_handler = RequestTracker()

    def __call__(self, request):
        response = self.get_response(request)
        self.page_view_handler.register_request(request)
        return response
