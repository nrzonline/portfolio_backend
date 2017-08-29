from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers

from projects.viewsets import (
    ProjectViewSet)#, AttachmentViewSet, ImageViewSet, LinkViewSet)
from accounts.viewsets import AccountViewSet
from skills.viewsets import SkillViewSet, SkillCategoryViewSet
from contact.viewsets import ContactMessageViewSet
from about.viewsets import AboutViewSet


router = routers.DefaultRouter()
router.register(r'account', AccountViewSet, base_name='accounts')
router.register(r'project', ProjectViewSet, base_name='projects')
# router.register(r'project-image', ImageViewSet, base_name='images')
# router.register(r'project-attachment', AttachmentViewSet, base_name='attachments')
# router.register(r'project-link', LinkViewSet, base_name='links')
router.register(r'skill', SkillViewSet, base_name='skills')
router.register(r'skill-category', SkillCategoryViewSet, base_name='categories')
router.register(r'contact-message', ContactMessageViewSet, base_name='contact-messages')
router.register(r'about', AboutViewSet, base_name='about')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

