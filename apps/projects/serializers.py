from rest_framework import serializers

from projects.models import (
     Project, ProjectAttachment, ProjectImage, ProjectLink)
from skills.serializers import SimpleSkillSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        exclude = ('is_published', 'project', 'datetime_added', 'datetime_modified', 'user', )


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

    published_images = SimpleImageSerializer(read_only=True, many=True)


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('user', 'is_published',)

    skills = SimpleSkillSerializer(read_only=True, many=True)
    published_images = ImageSerializer(read_only=True, many=True)
    published_attachments = AttachmentSerializer(read_only=True, many=True)
    published_links = LinkSerializer(read_only=True, many=True)
