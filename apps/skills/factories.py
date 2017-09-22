import factory

from skills.models import Skill, SkillCategory


class SkillCategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = SkillCategory

    title = "Title"
    description = "Description"
    frontend_position = 1


class SkillFactory(factory.DjangoModelFactory):
    class Meta:
        model = Skill
        django_get_or_create = ('title', )

    title = "Title"
    description = "Description"
    content = "Content body"
    category = factory.SubFactory(SkillCategoryFactory)
    level_max = 5
    level = 5
    is_published = True
    image = factory.django.ImageField()
