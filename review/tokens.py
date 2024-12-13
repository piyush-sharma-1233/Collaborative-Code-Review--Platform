# review/tokens.py

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

def get_tokens_for_user(user):
    """
    Generates JWT token pair (access & refresh) for the given user.
    """
    refresh = RefreshToken.for_user(user)
    access_token = AccessToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(access_token)
    }
