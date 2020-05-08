from django.shortcuts import render
from .serializers import PositionSerializer, EducationSerializer
from .serializers import CourseSerializer, SkillSerializer, InfoSerializer 
from .models import Position, Education, Course, Skill, Info
from rest_framework import viewsets

# VIEWSETS
class PositionViewSet(viewsets.ModelViewSet):

    queryset = Position.objects.filter(disabled=False) \
                               .order_by('-order')
    serializer_class = PositionSerializer

class EducationViewSet(viewsets.ModelViewSet):

    queryset = Education.objects.filter(disabled=False) \
                                .order_by('-order')
    serializer_class = EducationSerializer


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.filter(disabled=False) \
                               .order_by('-completion_date')

    serializer_class = CourseSerializer

class SkillViewSet(viewsets.ModelViewSet):

    queryset = Skill.objects.filter(disabled=False) \
                               .order_by('-order')

    serializer_class = SkillSerializer

class InfoViewSet(viewsets.ModelViewSet):

    queryset = Info.objects.filter(disabled=False) \
                               .order_by('order')
    serializer_class = InfoSerializer

