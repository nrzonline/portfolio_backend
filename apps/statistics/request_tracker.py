from django.conf import settings
from django.db.models import F

from statistics.models import RequestCount
from core.services import get_ip_address


class RequestTracker(object):
    def register_request(self, request):
        register_data = self.get_registrable_data_from_request(request)

        if register_data:
            self.save_request(register_data)

    def get_registrable_data_from_request(self, request):
        path_elements = self.extract_path_elements(request.path)

        if len(path_elements) > 0:
            module = path_elements[0]
            if not self.is_module_in_ignored_modules_list(module):
                return {
                    'module': module,
                    'path': '%s' % '/'.join(path_elements),
                    'ip_address': get_ip_address(request)
                }
            return
        return

    @staticmethod
    def extract_path_elements(path):
        path_split = path.split('/')

        # Remove first and last elements if they are empty
        if path_split[0] is u'':
            del path_split[0]
        if path_split[-1] is u'':
            del path_split[-1]
        return path_split

    @staticmethod
    def is_module_in_ignored_modules_list(module):
        return module and module in settings.STATISTICS_IGNORED_MODULES

    @staticmethod
    def save_request(register_data):
        request_record, _created = RequestCount.objects.get_or_create(**register_data)
        if not _created:
            request_record.hit_count = F('hit_count') + 1
            request_record.save()
