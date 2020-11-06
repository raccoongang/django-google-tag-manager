from django.conf import settings
from django.template import Library

from gtm.models import GTMConfiguration


register = Library()
ri = register.inclusion_tag


def gtm_tag(context, google_tag_id=None):
    request = context.get('request')
    if request:
        if request.COOKIES.get(
                getattr(settings, 'GOOGLE_TAG_BYPASS_COOKIE', None)):
            return

        if google_tag_id is None:
            current_configuration = GTMConfiguration.get_current_config(request)
            if current_configuration:
                google_tag_id = current_configuration.gtm_id

    if google_tag_id is None:
        google_tag_id = getattr(settings, 'GOOGLE_TAG_ID', None)

    context['google_tag_id'] = google_tag_id

    return context


ri("gtm/gtm.html", name='gtm', takes_context=True)(gtm_tag)
ri("gtm/gtm_head.html", name='gtm_head', takes_context=True)(gtm_tag)
ri("gtm/gtm_body.html", name='gtm_body', takes_context=True)(gtm_tag)
