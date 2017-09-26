from statistics.request_tracker import RequestTracker


class RequestStatisticsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        self.request_tracker = RequestTracker()

    def __call__(self, request):
        response = self.get_response(request)
        self.request_tracker.register_request(request)
        return response
