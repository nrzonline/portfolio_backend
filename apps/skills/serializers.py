from rest_framework import serializers

from skills.models import Skill, SkillCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        exclude = ()


class SkillSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Skill
        exclude = (
            'width',
            'height',
        )


class FlatSkillSerializer(SkillSerializer):
    category = None
