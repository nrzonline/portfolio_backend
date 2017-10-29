from rest_framework import serializers

from projects.models import Project
from multimedia.serializers import \
    ImageSerializer, SimpleImageSerializer, FileSerializer, LinkSerializer
from skills.serializers import FlatSkillSerializer


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
    published_files = FileSerializer(many=True)
    published_links = LinkSerializer(many=True)
