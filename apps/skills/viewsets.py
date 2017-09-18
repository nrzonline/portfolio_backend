from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from skills.serializers import SkillSerializer, CategorySerializer
from skills.models import Skill, SkillCategory


class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category',)
    queryset = Skill.objects.filter(is_published=True).order_by('-level')


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = SkillCategory.objects.filter(is_published=True).order_by('frontend_position')

