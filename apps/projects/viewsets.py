from rest_framework import viewsets

from projects.models import (
    Project, ProjectAttachment, ProjectImage, ProjectLink)
from projects.serializers import (
    ProjectSerializer, ImageSerializer, AttachmentSerializer, LinkSerializer)


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.filter(is_published=True)


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = ProjectImage.objects.filter(is_published=True)


class AttachmentViewSet(viewsets.ModelViewSet):
    serializer_class = AttachmentSerializer
    queryset = ProjectAttachment.objects.filter(is_published=True)


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = ProjectLink.objects.filter(is_published=True)
