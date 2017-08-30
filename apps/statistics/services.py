from django.conf import settings

from utils.services import get_ip_address


def get_registrable_data_from_request(request):
    request_path = request.path

    if settings.API_PATH not in request_path:
        return None
    else:
        path_split = request_path.split('/')
        # drop ['', 'api']
        del path_split[:2]

        return {
            'module': path_split[0],
            'path': '/%s' % '/'.join(path_split),
            'ip_address': get_ip_address(request)
        }
