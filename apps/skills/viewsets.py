from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from skills.serializers import SkillSerializer, SkillCategorySerializer
from skills.models import Skill, SkillCategory


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    queryset = Skill.objects.filter(is_published=True)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category',)


class SkillCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SkillCategorySerializer
    queryset = SkillCategory.objects.all().order_by('frontend_position')
