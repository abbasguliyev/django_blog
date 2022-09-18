import jwt
from django.conf import settings


def jwt_decode_handler(token):
    """
    JWT token create eden funksiya
    """
    secret_key = settings.SECRET_KEY
    
    return jwt.decode(
        token,
        secret_key,
        audience=settings.SIMPLE_JWT.get("AUDIENCE"),
        issuer=settings.SIMPLE_JWT.get("ISSUER"),
        algorithms=[settings.SIMPLE_JWT.get("ALGORITHM")]
    )