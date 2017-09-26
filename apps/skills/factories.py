import factory

from users.factories import UserFactory
from skills.models import Skill, SkillCategory


class SkillCategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = SkillCategory

    title = "Title"
    description = "Description"
    position = 1
    created_by = factory.SubFactory(UserFactory)


class SkillFactory(factory.DjangoModelFactory):
    class Meta:
        model = Skill
        django_get_or_create = ('title', )

    title = "Title"
    description = "Description"
    content = "Content body"
    category = factory.SubFactory(SkillCategoryFactory)
    level_max = 10
    level = 8
    is_published = True
    image = factory.django.ImageField()
    created_by = factory.SubFactory(UserFactory)
