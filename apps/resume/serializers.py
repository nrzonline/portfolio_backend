from rest_framework import serializers

from resume.models import Work, WorkImage, Education, Interest


class WorkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkImage
        exclude = (
            'width',
            'height',
            'work',
        )


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        exclude = (
            'width',
            'height',
        )

    primary_image = WorkImageSerializer(allow_null=True)
    images = WorkImageSerializer(many=True, allow_null=True)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ()


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        exclude = ()
