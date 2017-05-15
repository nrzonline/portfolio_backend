from rest_framework import serializers

from accounts.serializers import AccountSerializer
from projects.models import (
    Project, ProjectAttachment, ProjectImage, ProjectLink)
from skills.serializers import SkillSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        exclude = ()


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAttachment
        exclude = ()


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLink
        exclude = ()


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ()

    user = AccountSerializer()
    skills = SkillSerializer(read_only=True, many=True)
    published_images = ImageSerializer(read_only=True, many=True)
    published_attachments = AttachmentSerializer(read_only=True, many=True)
    published_links = LinkSerializer(read_only=True, many=True)

