from rest_framework import serializers

from resume.models import Work, WorkImage, Education, Interest


class WorkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkImage
        exclude = ('is_published', 'width', 'height', 'work', 'user')


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        exclude = ('is_published', 'width', 'height',)

    primary_image = WorkImageSerializer(allow_null=True)
    images = WorkImageSerializer(many=True, allow_null=True)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ('is_published',)


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        exclude = ('is_published',)
