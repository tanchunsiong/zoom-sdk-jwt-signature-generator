
#pip3 install pyjwt
import jwt
import hashlib
import hmac
import base64
import time
import random
def generateSignature(data,secret):
    encoded_jwt = jwt.encode(data, secret, algorithm="HS256")
    return (encoded_jwt);
if __name__ == '__main__':
    epoch_time = int(time.time())
    epoch_time_48hours_later=epoch_time+172800
    SDK_SECRET="enter your SDK secret here"
    APP_KEY="enter your App key here"
    randomnumber=random.randint(10000000,99999999)
    sessionName="sessname" + str(randomnumber)
    data = {"app_key": APP_KEY,
            "version": 1,
            "role_type": 1,
            "user_identity": "User ID",
            "session_key": "Session key",
            "iat": epoch_time,
            "exp": epoch_time_48hours_later, 
            "tpc": sessionName
            }
    data2 = {"app_key": APP_KEY,
            "version": 1,
            "role_type": 0,
            "user_identity": "User ID",
            "session_key": "Session key",
            "iat": epoch_time,
            "exp": epoch_time_48hours_later, 
            "tpc": sessionName
            }    
    print ("")        
    print ("Role 1")        
    print (generateSignature(data,SDK_SECRET))
    print ("")
    print ("Role 0")        
    print (generateSignature(data,SDK_SECRET))
    print ("")
    print (sessionName)
    print ("")
