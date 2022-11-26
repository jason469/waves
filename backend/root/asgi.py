import os
from datetime import timedelta

from backend.version import version
from django.apps import apps
from . import settings
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware
from django.core.cache import caches

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.root.settings")
apps.populate(settings.INSTALLED_APPS)

from backend.api.v1.endpoints.router import api_router as api_router_v1
from backend.api.auth.endpoints.router import auth_router


_application = get_wsgi_application()


def application(environ, start_response):
    script_name = getattr(settings, 'FORCE_SCRIPT_NAME', None)
    if script_name:
        environ['SCRIPT_NAME'] = script_name
        path_info = environ['PATH_INFO']
        if path_info.startswith(script_name):
            environ['PATH_INFO'] = path_info[len(script_name):]

    scheme = environ.get('HTTP_X_SCHEME', '')
    if scheme:
        environ['wsgi.url_scheme'] = scheme

    return _application(environ, start_response)


def get_fastapi_application() -> FastAPI:
    fastapi = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=version,
        root_path=settings.FASTAPI_ROOT_PATH,
    )
    fastapi.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    fastapi.include_router(auth_router, prefix='/api', tags=["/api"])
    fastapi.include_router(api_router_v1, prefix='/api/v1', tags=["/api/v1"])
    fastapi.mount('/', WSGIMiddleware(_application))
    return fastapi


app = get_fastapi_application()


@AuthJWT.load_config
def auth_jwt_config():
    class AuthJWTConfig(BaseModel):
        authjwt_secret_key: str = settings.AUTH_JWT_SECRET_KEY
        authjwt_denylist_enabled: bool = True
        authjwt_denylist_token_checks: set = {"access", "refresh"}
        authjwt_access_token_expires: timedelta = settings.AUTH_JWT_ACCESS_EXPIRY
        authjwt_refresh_token_expires: timedelta = settings.AUTH_JWT_REFRESH_EXPIRY

    return AuthJWTConfig()


@app.exception_handler(AuthJWTException)
def auth_jwt_exception_handler(_: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    jti = decrypted_token['jti']
    auth_cache = caches[settings.AUTH_CACHE_NAME]
    entry = auth_cache.get(jti)
    return entry and entry is True
