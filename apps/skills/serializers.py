from rest_framework import serializers

from skills.models import Skill, SkillCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        exclude = ()


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ('width', 'height', 'is_published',)

    category = CategorySerializer()


class SkillWithoutCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'title', 'image', 'level_max', 'level', 'slug', )


class CategorizedSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        exclude = ()

    skills = SkillWithoutCategorySerializer(many=True)

