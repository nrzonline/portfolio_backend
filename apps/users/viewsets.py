from django.contrib.auth.models import User
from rest_framework import viewsets

from users.serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = User.objects.all()

