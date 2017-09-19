from rest_framework import serializers

from skills.models import Skill, SkillCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        exclude = ('is_published', )


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ('width', 'height', 'is_published',)

