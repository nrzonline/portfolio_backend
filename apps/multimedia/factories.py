import factory

from core.factories.mixins import ContentTypeFactoryMixin
from users.factories import UserFactory
from multimedia.models import Image, File, Link


class ImageFactory(ContentTypeFactoryMixin, factory.DjangoModelFactory):
    class Meta:
        model = Image

    title = "Title"
    description = "Description"
    image = factory.django.ImageField()
    is_primary = True
    is_published = True
    created_by = factory.SubFactory(UserFactory)


class FileFactory(ContentTypeFactoryMixin, factory.DjangoModelFactory):
    class Meta:
        model = File

    title = "Title"
    description = "Description"
    file = factory.django.FileField()
    is_published = True
    created_by = factory.SubFactory(UserFactory)


class LinkFactory(ContentTypeFactoryMixin, factory.DjangoModelFactory):
    class Meta:
        model = Link

    title = "Title"
    description = "Description"
    url = 'http://test-portfolio.com'
    is_published = True
    created_by = factory.SubFactory(UserFactory)
