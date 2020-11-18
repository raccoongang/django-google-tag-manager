django-google-tag-manager
=========================

Template tag to install your Google Tag Manager account in your
templates (http://www.google.com/tagmanager/)

## Installation and Usage

1. run `pip install -e git+https://github.com/raccoongang/django-google-tag-manager.git@<version_you_need>#egg=django-google-tag-manager`
2. add `gtm.apps.GoogleTagManagerConfig` to your `INSTALLED_APPS` setting.
3. apply migrations by running the Django `migrate` manage.py command.
4. add `{% load gtm_tags %}` then add `{% gtm_head %}` between `<head>` and `</head>` then add `{% gtm_body %}` between `<body>` and `</body>`
5. You can add GTM ID by doing one of the next three options:
    1. pass GTM ID when loading templatetags like `{% gtm_head "GTM-ABC123" %}` and `{% gtm_body "GTM-ABC123" %}`.
    2. set the GTM ID in Django admin, it's called the "Google Tag Manager" section. You can set the GTM ID for each site separately.
    3. set `GOOGLE_TAG_ID` into your settings.

All of them have a priority in the same order they are described.

That's it for the most part. If for any reason you want to override
the templates used to render the tags, they are called
`gtm/gtm_head.html` and `gtm/gtm_body.html`.

For backwards compatibility you can still use the single `{% gtm %}`
tag just below your `<body>` opening tag. This will output both the
head and body code.
