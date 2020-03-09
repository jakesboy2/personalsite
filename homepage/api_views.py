from rest_framework import viewsets, permissions
from . import models
from . import serializers

class ExampleUsersViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.ExampleUsers.objects.all()
    serializer_class = serializers.ExampleUsersSerializer

class ExampleCitationsViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.ExampleCitations.objects.all()
    serializer_class = serializers.ExampleCitationsSerializer