from fastapi import Depends
from fastapi_jwt_auth import AuthJWT


def valid_refresh(auth: AuthJWT = Depends()):
    auth.jwt_refresh_token_required()
    return auth


def valid_access(auth: AuthJWT = Depends()):
    auth.jwt_required()
    return auth