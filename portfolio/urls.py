from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers

from projects.viewsets import ProjectViewSet
from accounts.viewsets import AccountViewSet
from skills.viewsets import SkillViewSet, SkillCategoryViewSet
from contact.viewsets import ContactMessageCustomErrorMessagesViewSet
from profiles.viewsets import ProfileViewSet
from votes.viewsets import VoteViewSet
from statistics.viewsets import RequestCountViewSet
from resume.viewsets import WorkViewSet, EducationViewSet, InterestViewSet


router = routers.DefaultRouter()
router.register(r'account', AccountViewSet, base_name='account')
router.register(r'project', ProjectViewSet, base_name='project')
router.register(r'skill', SkillViewSet, base_name='skill')
router.register(r'skill-category', SkillCategoryViewSet, base_name='categories')
router.register(r'contact-message', ContactMessageCustomErrorMessagesViewSet, base_name='contact-message')
router.register(r'profile', ProfileViewSet, base_name='profile')
router.register(r'work', WorkViewSet, base_name='work')
router.register(r'education', EducationViewSet, base_name='education')
router.register(r'interest', InterestViewSet, base_name='interest')

get_object_votes = VoteViewSet.as_view({'get': 'get_object_votes'})
cast_object_vote = VoteViewSet.as_view({'get': 'cast_object_vote'})

request_count = RequestCountViewSet.as_view({'get': 'get_request_count'})
unique_request_count = RequestCountViewSet.as_view({'get': 'get_unique_request_count'})


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),

    url(r'^vote/(?P<model>\w+)/(?P<object_id>\d+)/(?P<vote>\d+)/cast/$', cast_object_vote),
    url(r'^vote/(?P<model>\w+)/(?P<object_id>\d+)/$', get_object_votes),

    url(r'^request-count/unique/$', unique_request_count),
    url(r'^request-count/(?P<path>[-/a-z0-9]+)/unique/$', unique_request_count),
    url(r'^request-count/$', request_count),
    url(r'^request-count/(?P<path>[-/a-z0-9]+)/$', request_count),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

