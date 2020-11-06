from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site


class GTMConfiguration(models.Model):
    site = models.OneToOneField(Site)
    gtm_id = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'GTM Configurations'

    @staticmethod
    def get_current_config(request):
        current_site = get_current_site(request)
        try:
            return GTMConfiguration.objects.get(site=current_site.id)
        except GTMConfiguration.DoesNotExist:
            return None
