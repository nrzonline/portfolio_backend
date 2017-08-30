from django.db.models import F

from statistics.models import RequestCount
from statistics.services import get_registrable_data_from_request


class RequestCountTracker(object):
    def register_request(self, request):
        register_data = get_registrable_data_from_request(request)

        if register_data:
            exceptions_applied_register_data = self.modify_data_for_exceptions(register_data)
            self.register_request_count(exceptions_applied_register_data)

    @staticmethod
    def register_request_count(register_data):
        page_view_record, _created = RequestCount.objects.get_or_create(**register_data)
        if not _created:
            page_view_record.count = F('count') + 1
            page_view_record.save()

    @staticmethod
    def modify_data_for_exceptions(register_data):
        if register_data['module'] == 'request-count':
            new_path = '/request-count/'
            if 'unique' in register_data['path']:
                new_path = '/request-count/unique/'
            register_data['path'] = new_path
        return register_data

