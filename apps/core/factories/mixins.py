from django.contrib.contenttypes.models import ContentType
import factory

from projects.factories import ProjectFactory


class ContentTypeFactoryMixin(factory.DjangoModelFactory):
    class Meta:
        abstract = True

    content_type = factory.LazyAttribute(
        lambda obj: ContentType.objects.get_for_model(obj.content_object))
    object_id = factory.SelfAttribute('content_object.id')
    content_object = factory.SubFactory(ProjectFactory)
