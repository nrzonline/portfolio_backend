from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers

from projects.viewsets import (
    ProjectViewSet, AttachmentViewSet, ImageViewSet, LinkViewSet)
from accounts.viewsets import AccountViewSet
from skills.viewsets import SkillViewSet, SkillCategoryViewSet
from contact.viewsets import ContactDetailViewSet, ContactMessageViewSet


router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet, base_name='accounts')
router.register(r'projects', ProjectViewSet, base_name='projects')
router.register(r'project-images', ImageViewSet, base_name='images')
router.register(r'project-attachments', AttachmentViewSet,
                base_name='attachments')
router.register(r'project-links', LinkViewSet, base_name='links')
router.register(r'skills', SkillViewSet, base_name='skills')
router.register(r'skill-categories', SkillCategoryViewSet,
                base_name='categories')
router.register(r'contact', ContactDetailViewSet, base_name='contact')
router.register(r'contact-messages', ContactMessageViewSet,
                base_name='contact-messages')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

