from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class CustomInvalidToken(InvalidToken):
    status_code = 444


class Authentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        try:
            return super().get_validated_token(raw_token)

        except InvalidToken as e:
            raise CustomInvalidToken()