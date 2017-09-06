from rest_framework import viewsets

from resume.models import Work, Education, Interest
from resume.serializers import WorkSerializer, EducationSerializer, InterestSerializer


class WorkViewSet(viewsets.ModelViewSet):
    serializer_class = WorkSerializer
    queryset = Work.objects.filter(is_published=True).order_by('-date_from')


class EducationViewSet(viewsets.ModelViewSet):
    serializer_class = EducationSerializer
    queryset = Education.objects.filter(is_published=True).order_by('-date_from')


class InterestViewSet(viewsets.ModelViewSet):
    serializer_class = InterestSerializer
    queryset = Interest.objects.filter(is_published=True)
