from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from skills.serializers import FlatSkillSerializer, SkillSerializer, CategorySerializer
from skills.models import Skill, SkillCategory


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category',)
    queryset = Skill.objects.filter(is_published=True).order_by('-level')

    def get_serializer_class(self):
        if self.action == 'list':
            return FlatSkillSerializer
        return SkillSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = SkillCategory.objects.filter(is_published=True).order_by('position')

