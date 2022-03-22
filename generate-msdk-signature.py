
#pip3 install pyjwt
import jwt
import hashlib
import hmac
import base64
import time
def generateSignature(data,secret):
    encoded_jwt = jwt.encode(data, secret, algorithm="HS256")
    return (encoded_jwt);
if __name__ == '__main__':
    epoch_time = int(time.time())
    epoch_time_48hours_later=epoch_time+172800
    SDK_SECRET="enter your secret here"
    APP_KEY="enter your app key here"
    data = { "appKey": APP_KEY,
             "iat": epoch_time, 
             "exp": epoch_time_48hours_later, 
             "tokenExp": epoch_time_48hours_later 
            }
    print (generateSignature(data,SDK_SECRET))
