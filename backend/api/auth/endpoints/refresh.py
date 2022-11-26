from datetime import datetime
from fastapi import Depends
from backend.api.auth.endpoints.router import auth_router
from backend.api.auth.schemas import TokenPair
from backend.api.auth.dependencies import valid_refresh
from backend.api.auth.util import generate_token_pair


@auth_router.post('/refresh', response_model=TokenPair)
def refresh(auth=Depends(valid_refresh)):
    old_refresh_expiry_timestamp = auth.get_raw_jwt()['exp']
    time_till_refresh_expiry = datetime.fromtimestamp(old_refresh_expiry_timestamp) - datetime.now()
    return generate_token_pair(auth, auth.get_jwt_subject(), time_till_refresh_expiry.seconds)