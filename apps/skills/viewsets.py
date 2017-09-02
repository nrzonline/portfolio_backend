from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from skills.serializers import SkillSerializer, CategorizedSkillsSerializer, CategorySerializer
from skills.models import Skill, SkillCategory


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category',)
    queryset = Skill.objects.filter(is_published=True).order_by('-level')


class SkillCategoryViewSet(viewsets.ModelViewSet):
    queryset = SkillCategory.objects.all().order_by('frontend_position')

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorizedSkillsSerializer
        return CategorySerializer

