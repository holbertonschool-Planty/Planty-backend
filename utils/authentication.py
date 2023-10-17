from ninja.security import HttpBearer
from utils.models_loads import get_usersToken_model

class TokenAuth(HttpBearer):
    def authenticate(self, request, token):
        try:
            token_obj = get_usersToken_model().objects.get(token=token)
            return token_obj.user
        except get_usersToken_model().DoesNotExist:
            return None
