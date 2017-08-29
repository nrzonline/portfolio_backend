from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from skills.serializers import SkillSerializer, SimpleSkillSerializer, SkillCategorySerializer
from skills.models import Skill, SkillCategory


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category',)
    queryset = Skill.objects.filter(is_published=True).order_by('-level')

    def get_serializer_class(self):
        if self.action == 'list':
            return SkillSerializer
        return SimpleSkillSerializer


class SkillCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SkillCategorySerializer
    queryset = SkillCategory.objects.all().order_by('frontend_position')
