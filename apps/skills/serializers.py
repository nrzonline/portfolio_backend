from rest_framework import serializers

from skills.models import Skill, SkillCategory


class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        exclude = ()


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ('width', 'height', )

    category = SkillCategorySerializer()