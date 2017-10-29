from rest_framework import serializers

from multimedia.models import Image, File, Link


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = (
            'width',
            'height',
        )


class SimpleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'title',
            'image',
        )


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = ()


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        exclude = ()


