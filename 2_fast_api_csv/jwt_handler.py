# This files responsible for signing, encoding, deconding and returning JWTs.

import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# Function returns the generated Tokens (JWTs)
def token_response(token : str):
    return {
        "acess token": token
    }

# Function used for signing the JWT string
def signJWT(userID : str):
    payload = {
        "userID" : userID,
        "expires" : time.time() + 600
    }
    token = jwt.encode(payload,
                       JWT_SECRET,
                       algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token : str):
    try:
        decode_token = jwt.decode(token,
                                JWT_SECRET,
                                algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}
    

'''
import jwt
from datetime import datetime, timedelta
from typing import Dict, Optional

class JWTHandler:
    def __init__(self, secret_key: str, algorithm: str = "HS256", access_token_expire_minutes: int = 30):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes

    def create_access_token(self, data: Dict, expires_delta: Optional[timedelta] = None) -> str:
        """
        Create a new JWT access token
        """
        to_encode = data.copy()
        
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        
        return encoded_jwt

    def verify_token(self, token: str) -> Dict:
        """
        Verify the JWT token and return the decoded payload
        """
        try:
            decoded_token = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.JWTError:
            raise ValueError("Invalid token")
'''