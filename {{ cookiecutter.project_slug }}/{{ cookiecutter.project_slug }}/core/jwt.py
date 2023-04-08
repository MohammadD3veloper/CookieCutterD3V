"""
Any integrations to jwt will placed here
eg: create/revoke/delete jwt tokens
"""

from rest_framework_simplejwt.tokens import RefreshToken


def generate_user_token(user):
    """ Generate token for each user """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def blacklist_user_token(token):
    """ Set user token to blacklist """
    token = RefreshToken(token)
    token.blacklist()
    return token
