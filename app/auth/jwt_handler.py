import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {"access token": token}


def sign_jwt(userId: str):
    payload = {"userId": userId, "expiry": time.time() + 600}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decoded_token if decoded_token["expires"] > time.time() else None
    except ValueError:
        return
