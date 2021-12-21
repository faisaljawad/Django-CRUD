import jwt
from rest_framework import authentication
from django.conf import settings

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None
        prefix, token = auth_data.decode('utf-8').split(' ')
        try:
            payload=jwt.deocde(token, settings.JWT_SECRET_KEY)
        except expression as identifier:
            pass
        return super().authenticate(request)