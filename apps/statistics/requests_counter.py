from django.conf import settings
from django.db.models import F

from statistics.models import RequestCount
from utils.services import get_ip_address


class RequestTracker(object):
    def register_request(self, request):
        register_data = self.get_registrable_data_from_request(request)

        if register_data:
            exceptions_applied_register_data = self.modify_data_for_exceptions(register_data)
            self.register_request_count(exceptions_applied_register_data)

    def get_registrable_data_from_request(self, request):
        path_elements_list = self.get_path_elements_list(request.path)

        if len(path_elements_list) > 0:
            module = path_elements_list[0]
            if not self.is_module_in_ignored_modules_list(module):
                return {
                    'module': module,
                    'path': '%s' % '/'.join(path_elements_list),
                    'ip_address': get_ip_address(request)
                }
            return
        return

    @staticmethod
    def get_path_elements_list(path):
        path_split = path.split('/')
        del path_split[:1]  # first element is always ''
        del path_split[-1]  # last element is always ''
        return path_split

    @staticmethod
    def is_module_in_ignored_modules_list(module):
        return module and module in settings.STATISTICS_IGNORED_MODULES

    @staticmethod
    def register_request_count(register_data):
        page_view_record, _created = RequestCount.objects.get_or_create(**register_data)
        if not _created:
            page_view_record.count = F('count') + 1
            page_view_record.save()

    @staticmethod
    def modify_data_for_exceptions(register_data):
        # if register_data['module'] == 'request-count':
        #     if 'unique' in register_data['path']:
        #         register_data['path'] = 'request-count/unique/<path>'
        return register_data
