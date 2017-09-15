from django.conf import settings

from utils.services import get_ip_address


def get_registrable_data_from_request(request):
    request_path = request.path

    path_split = request_path.split('/')
    del path_split[:1]
    module = path_split[0]

    if module in settings.STATISTICS_IGNORE_MODULES:
        return

    return {
        'module': path_split[0],
        'path': '/%s' % '/'.join(path_split),
        'ip_address': get_ip_address(request)
    }
