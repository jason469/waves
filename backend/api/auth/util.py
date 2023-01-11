from typing import Optional

from django.core.cache import caches
from fastapi_jwt_auth import AuthJWT
from backend.api.auth.schemas import TokenPair
from backend.config import settings

auth_cache = caches[settings.AUTH_CACHE_NAME]

ACCESS_TOKEN_CACHE_KEY = "AT({0})"
REFRESH_TOKEN_CACHE_KEY = "RT({0})"


def add_old_tokens_to_denylist(auth: AuthJWT, username: str):
    if old_AT := auth_cache.get(ACCESS_TOKEN_CACHE_KEY.format(username)):
        old_AT_decoded = auth.get_raw_jwt(old_AT)
        auth_cache.set(old_AT_decoded['jti'], True, timeout=settings.AUTH_JWT_ACCESS_EXPIRY.seconds)

    if old_RT := auth_cache.get(REFRESH_TOKEN_CACHE_KEY.format(username)):
        old_RT_decoded = auth.get_raw_jwt(old_RT)
        auth_cache.set(old_RT_decoded['jti'], True, timeout=settings.AUTH_JWT_REFRESH_EXPIRY.seconds)


def generate_token_pair(auth: AuthJWT, subject: str, refresh_expires: Optional[int] = None) -> TokenPair:
    add_old_tokens_to_denylist(auth, subject)
    access_token = auth.create_access_token(subject=subject)
    refresh_token = auth.create_refresh_token(subject=subject, expires_time=refresh_expires)
    auth_cache.set(ACCESS_TOKEN_CACHE_KEY.format(subject), access_token)
    auth_cache.set(REFRESH_TOKEN_CACHE_KEY.format(subject), refresh_token)
    return TokenPair(access_token=access_token, refresh_token=refresh_token)