from rest_framework import serializers
from . import models

class ExampleUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExampleUsers
        fields = ('id', 'first_name', 'last_name')

class ExampleCitationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExampleCitations
        fields = ('id', 'citation_number', 'date_given', 'given_by')