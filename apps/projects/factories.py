import factory

from users.factories import UserFactory
from projects.models import Project


class ProjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = Project
        django_get_or_create = ('title', )

    title = "Title"
    description = "Description"
    content = "Content"
    url = "http://test-portfolio.com"
    is_published = True
    created_by = factory.SubFactory(UserFactory)
