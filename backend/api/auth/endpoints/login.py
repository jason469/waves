from django.contrib.auth import authenticate
from fastapi import Depends, HTTPException, status
from fastapi_jwt_auth import AuthJWT
from backend.api.auth.endpoints.router import auth_router
from backend.api.auth.schemas import TokenPair, Credentials
from backend.api.auth.util import generate_token_pair


@auth_router.post('/login', response_model=TokenPair)
def login(creds: Credentials, auth: AuthJWT = Depends()):
    if authenticate(username=creds.username, password=creds.password) is None:
        msg = "Incorrect username or password"
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=msg,
            headers={"WWW-Authenticate": "Bearer"},
        )
    return generate_token_pair(auth, creds.username)

