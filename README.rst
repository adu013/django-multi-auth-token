
django-multi-auth-token

This package allows multi token authentication for Django Rest Framework(DRF)


Quick start
-----------
1. Add "multi_auth_token" to your INSTALLED_APPS setting like this::
``
INSTALLED_APPS = [
...
'multi_auth_token',
]
``

2. Add "multi_auth_token.authentication.MultiTokenAuthentication" to "DEFAULT_AUTHENTICATION_CLASSES" like this:
``
REST_FRAMWORK = {
'DEFAULT_AUTHENTICATION_CLASSES': [
'multi_auth_token.authentication.MultiTokenAuthentication',
...
]
}
``

3. Migrate
``
python manage.py migrate
``


IMPORTANT
---------
1. DO NOT add "rest_framework.authtoken" to your INSTALLED_APPS.
2. DO NOT add "rest_framework.authentication.TokenAuthentication" to DEFAULT_AUTHENTICATION_CLASSES


TODO
----


Changelog
---------
1.0.0 - 2023-03-01 Arindam Dutta - First release


Copyright(c) 2023 Arindam Dutta
