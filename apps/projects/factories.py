import factory

from accounts.factories import UserFactory
from projects.models import Project, ProjectImage, ProjectAttachment, \
    ProjectLink


class ProjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = Project
        django_get_or_create = ('title', )

    title = "Title"
    description = "Description"
    content = "Content"
    url = "http://test-portfolio.com"
    is_published = True
    user = factory.SubFactory(UserFactory)


class ProjectImageFactory(factory.DjangoModelFactory):
    class Meta:
        model = ProjectImage

    project = factory.SubFactory(ProjectFactory)
    title = "Title"
    description = "Description"
    image = factory.django.ImageField()
    created_by = factory.SubFactory(UserFactory)
    is_primary = True
    is_published = True


class ProjectAttachmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = ProjectAttachment

    project = factory.SubFactory(ProjectFactory)
    title = "Title"
    description = "Description"
    file = factory.django.FileField()
    created_by = factory.SubFactory(UserFactory)
    is_published = True


class ProjectLinkFactory(factory.DjangoModelFactory):
    class Meta:
        model = ProjectLink

    project = factory.SubFactory(ProjectFactory)
    title = "Title"
    description = "Description"
    url = 'http://test-portfolio.com'
    is_published = True
    created_by = factory.SubFactory(UserFactory)
