import factory

from users.factories import UserFactory
from resume.models import Work, WorkImage, Education, Interest
from datetime import datetime


class WorkFactory(factory.DjangoModelFactory):
    class Meta:
        model = Work
        django_get_or_create = ('title', )

    title = "Title"
    description = "Description"
    content = "Content"
    organization = "Organization"
    organization_image = factory.django.ImageField()
    date_from = datetime(2015, 1, 1)
    date_till = datetime(2017, 1, 1)
    created_by = factory.SubFactory(UserFactory)


class WorkImageFactory(factory.DjangoModelFactory):
    class Meta:
        model = WorkImage
        django_get_or_create = ('title', )

    work = factory.SubFactory(WorkFactory)
    title = "Title"
    description = "Description"
    image = factory.django.ImageField()
    created_by = factory.SubFactory(UserFactory)


class EducationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Education
        django_get_or_create = ('title', )

    title = "Title"
    description = "Description"
    content = "Content"
    date_from = datetime(2015, 1, 1)
    date_till = datetime(2017, 1, 1)
    created_by = factory.SubFactory(UserFactory)


class InterestFactory(factory.DjangoModelFactory):
    class Meta:
        model = Interest
        django_get_or_create = ('title', )

    title = "Title"
    description = "Description"
    content = "Content"
    created_by = factory.SubFactory(UserFactory)
