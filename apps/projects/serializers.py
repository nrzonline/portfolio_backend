from rest_framework import serializers

from projects.models import (
     Project, ProjectAttachment, ProjectImage, ProjectLink)
from skills.serializers import FlatSkillSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        exclude = (
            'width',
            'height',
        )


class SimpleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = (
            'id',
            'title',
            'image',
        )


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAttachment
        exclude = ()


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLink
        exclude = ()


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = (
            'description',
            'content',
            'url',
        )

    published_images = SimpleImageSerializer(many=True)


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ()

    skills = FlatSkillSerializer(many=True)
    primary_image = ImageSerializer()
    published_images = ImageSerializer(many=True)
    published_attachments = AttachmentSerializer(many=True)
    published_links = LinkSerializer(many=True)
