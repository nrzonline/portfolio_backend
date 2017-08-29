from rest_framework import viewsets


from projects.models import Project
from projects.serializers import ProjectListSerializer, ProjectDetailSerializer
from utils.services import get_ip_address


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(is_published=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        print('projects', pk, get_ip_address(self.request))

        return super(ProjectViewSet, self).retrieve(request, *args, **kwargs)


