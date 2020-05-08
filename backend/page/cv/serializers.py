from rest_framework import serializers
from .models import Position, Company
from .models import Education, Course, Skill, Info
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name']

    #  def to_representation(self):
    #      return self.company_name
    #
class PositionSerializer(serializers.ModelSerializer):
    # company = CompanySerializer(many=False)
    company = serializers.StringRelatedField(many=False)
    class Meta:
        model = Position
        exclude = ['disabled', 'order']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ['id', 'disabled', 'order']

#  class ProviderSerializer(serializers.ModelSerializer):
#      class Meta:
#          model = Provider
#          fields = ['name']

class CourseSerializer(serializers.ModelSerializer):
    provider = serializers.StringRelatedField(many=False)
    class Meta:
        model = Course
        exclude = ['id', 'disabled', 'order']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ['id', 'disabled', 'order']

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        exclude = ['id', 'disabled', 'order']
