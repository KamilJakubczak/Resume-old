from django.urls import path, include
from rest_framework import routers
from .views import PositionViewSet, EducationViewSet, CourseViewSet
from .views import SkillViewSet, InfoViewSet

router = routers.DefaultRouter()
router.register('positions', PositionViewSet)
router.register('educations', EducationViewSet)
router.register('courses', CourseViewSet)
router.register('skills', SkillViewSet)
router.register('info', InfoViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
