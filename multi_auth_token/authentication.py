# multi_auth_token/authentication.py
from rest_framework.authentication import TokenAuthentication

from .models import Token


class MultiTokenAuthentication(TokenAuthentication):
    model = Token
