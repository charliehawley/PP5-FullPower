from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Music(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    band = models.ForeignKey('Band', null=True, blank=True, on_delete=models.SET_NULL)
    embed_code = models.CharField(max_length=1024, null=True, blank=True)
    release_date = models.DateField()

    def __str__(self):
        return self.name
