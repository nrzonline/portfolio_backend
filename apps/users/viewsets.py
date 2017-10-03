from django.contrib.auth.models import User
from rest_framework import viewsets

from users.serializers import userSerializer


class userViewSet(viewsets.ModelViewSet):
    serializer_class = userSerializer
    queryset = User.objects.all()

