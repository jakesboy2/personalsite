from django.db import models

class ExampleUsers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class ExampleCitations(models.Model):
    citation_number = models.IntegerField()
    date_given = models.DateField()
    given_by = models.CharField(max_length=30)

