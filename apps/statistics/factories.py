import factory

from statistics.models import RequestCount


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = RequestCount
        django_get_or_create = ('module', 'path', 'ip_address',)

    module = "module"
    path = "/module/1/with-slug/"
    ip_address = "127.0.0.1"
