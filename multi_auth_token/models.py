# multi_auth_token/models.py
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token as AuthToken

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Token(AuthToken):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='auth_tokens'
    )
    identifier = models.CharField(max_length=128)
    key = models.CharField(max_length=64, db_index=True, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'identifier'),)
