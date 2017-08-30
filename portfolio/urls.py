from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers

from projects.viewsets import ProjectViewSet
from accounts.viewsets import AccountViewSet
from skills.viewsets import SkillViewSet, SkillCategoryViewSet
from contact.viewsets import ContactMessageViewSet
from about.viewsets import AboutViewSet
from statistics.viewsets import RequestCountViewSet

request_count = RequestCountViewSet.as_view({'get': 'get_request_count'})
unique_request_count = RequestCountViewSet.as_view({'get': 'get_unique_request_count'})

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet, base_name='accounts')
router.register(r'project', ProjectViewSet, base_name='projects')
router.register(r'skill', SkillViewSet, base_name='skills')
router.register(r'skill-category', SkillCategoryViewSet, base_name='categories')
router.register(r'contact-message', ContactMessageViewSet, base_name='contact-messages')
router.register(r'about', AboutViewSet, base_name='about')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^%s/' % settings.API_PATH, include(router.urls)),

    url(r'^%s/request-count/unique/$' % settings.API_PATH, unique_request_count),
    url(r'^%s/request-count/(?P<path>[-/a-z0-9]+)/unique/$' % settings.API_PATH, unique_request_count),
    url(r'^%s/request-count/$' % settings.API_PATH, request_count),
    url(r'^%s/request-count/(?P<path>[-/a-z0-9]+)/$' % settings.API_PATH, request_count),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

