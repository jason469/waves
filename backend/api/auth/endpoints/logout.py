from fastapi import Depends, status
from fastapi.responses import JSONResponse
from backend.api.auth.dependencies import valid_refresh
from backend.api.auth.endpoints.router import auth_router
from backend.api.auth.util import (
    add_old_tokens_to_denylist, auth_cache, ACCESS_TOKEN_CACHE_KEY, REFRESH_TOKEN_CACHE_KEY
)

# Logout is an example of using FastAPI's dependency injector, which simplifies the use of dependencies
# Through a mixture of path params, query params and request.body, we can assemble the information needed to create an AuthJWT object
# This information is passed into the valid_refresh function.
# In the valid_refresh function, we create an AuthJWT object, perform a jwt_refresh_token_required() call on it, and pass back the auth object
# The auth object is then used by the logout function

@auth_router.delete('/logout')
def logout(auth=Depends(valid_refresh)):
    username = auth.get_jwt_subject()
    add_old_tokens_to_denylist(auth, auth.get_jwt_subject())
    auth_cache.delete(ACCESS_TOKEN_CACHE_KEY.format(username))
    auth_cache.delete(REFRESH_TOKEN_CACHE_KEY.format(username))

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"detail": "logged out."}
    )
