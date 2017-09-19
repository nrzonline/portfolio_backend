from rest_framework import serializers

from projects.models import (
     Project, ProjectAttachment, ProjectImage, ProjectLink)
from skills.serializers import SkillSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        exclude = ('is_published', 'project', 'datetime_added', 'datetime_modified', 'user', 'is_primary',)


class SimpleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ('id', 'title', 'image',)


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
        fields = ('id', 'title', 'slug', 'is_published', 'published_images',)

    published_images = SimpleImageSerializer(many=True)


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('user', 'is_published',)

    skills = SkillSerializer(many=True)
    primary_image = ImageSerializer()
    published_images = ImageSerializer(many=True)
    published_attachments = AttachmentSerializer(many=True)
    published_links = LinkSerializer(many=True)
