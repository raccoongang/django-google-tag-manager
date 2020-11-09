from django.contrib import admin

from .models import GTMConfiguration

class GTMConfigurationAdmin(admin.ModelAdmin):
    list_display = ('site', 'gtm_id')


admin.site.register(GTMConfiguration, GTMConfigurationAdmin)
