# zoom-sdk-jwt-signature-generator
This python cli generates JWT Signature for Zoom Meeting SDK and Zoom Video SDK

The cli script written in python helps developers quicky generate JWT token based on their SDK Key and SDK Secret.

There are 2 types of signature which this generator create. Refer to the respective section below for more details

# Common feature across both scripts #
1. Zoom uses EPOCH time to determine start and end/expire date of the token. By default, the generator uses current time as **start** and +48 hours later as **end / expiry**
2. You will need to install the python library using the command 'pip3 install pyjwt'
3. You will need to enter your own SDK_Secret and App_Key found in your [Zoom Marketplace Account](https://marketplace.zoom.us)

## Generate vSDK Signature py script ##
This refers to generate-vsdk-signature.py file. After downloading this repo, you can run it in your shell via 'python3 generate-vsdk-signature.py'
The payload specification can be found on the [official zoom docs, auth for vSDK](https://marketplace.zoom.us/docs/sdk/video/auth/). Nonetheless I've included the snipplet below for easy reference

> app_key is the SDK Key found in the App Dashboard.
>
>version should be set to 1.
>role_type indicates the user’s role in a session: host or participant. As of the Video SDK version 1.2.0 and above, this is required for all users. You will get an invalid parameter error in the onError callback if this is not provided. This prevents a random participant from gaining host privileges if the host loses access. The role_type values are:
>
>
>0 — The user is a participant. Other users should be assigned to this role.
>1 — The user is the host. If you want the original host of the session to be able to regain host privileges after leaving and rejoining the session, you should not assign this to more than one user per session. If the user with this role leaves the session and rejoins, they will regain host privileges. user_identity is an available field to uniquely specify a user in your system. The maximum length is 15 characters. This field is optional.
>
>session_key is an available field to uniquely specify a session in your system, for example, to make reporting easier. This is a string. It will be present in APIs. This field is optional.
>
>iat is the timestamp of the token in seconds identifying when the JWT was issued. The value of this field should be in long format and should not be a string.
>
>exp shows the expiration time of the token in seconds since epoch. To process, the current date/time must be before the expiration date/time. Expiration times are limited to a maximum of two days (48 hours) from the current date/time.
>
>tpc is the name of the session that the user is going to create or join. It cannot be empty and supports a maximum of 200 characters. It can include the uppercase or lowercase English letters a to z, numbers 0 to 9, the space character, and the following symbols: !, #, $, %, &, (, ), +, -, :, ;, <, =, ., > >, ?, @, [, ], ^, _, {, }, |, ~, ,.
>
>{
>
>  "app_key": "SDK_KEY",
>  
>  "version": 1,
>  
>  "role_type": 0,
>  
>  "user_identity": "User ID", // optional
>  
>  "session_key": "Session key" // optional
>  
>  "iat": 0, //Provide the current timestamp as the value of this field.
>  
>  "exp": 0, //Timestamp expiration date (Max: 2 days) in epoch format.
>  
>  "tpc": "Session name, cannot be empty (Max: 200 characters)"
>  
>}

## Generate mSDK Signature py script ##
This refers to generate-msdk-signature.py file. After downloading this repo, you can run it in your shell via 'python3 generate-msdk-signature.py'
The payload specification can be found on the [official zoom docs, auth for mSDK](https://marketplace.zoom.us/docs/sdk/native-sdks/auth/). Similarly I've included the snipplet below for easy reference
>### Payload ###
>The payload of a JWT contains the claims of the token, or the pieces of information being passed about the user and any metadata required.
>
>appKey is the SDK Key found in the App Dashboard.
>
>iat is the timestamp of the token in seconds identifying when the JWT is issued. The value of this field should be in long format and should not be a string.
>
>tokenExp is when the SDK authentication session expires in epoch format. Must be at least 30 minutes (1800 seconds) greater than the token's iat field. When this expires, the SDK will trigger a callback informing your app that it needs to re-authenticate with an up-to-date JWT. There is no max value for this, but setting extremely long expiration windows is not recommended.
>
>exp is when the JWT itself expires in epoch format. Must be at least 30 minutes (1800 seconds) greater than the token's iat field. Max value of iat value + 48 hours (172,800 seconds).
>
>{
>
>  "appKey": "SDK_KEY",
>  
>  "iat": 0, //Provide the current timestamp as the value of this field.
>  
>  "exp": 0, //JWT expiration date (Min:1800 seconds greater than iat value, Max: 48 hours greater than iat value) in epoch format.
>  
>  "tokenExp": 0 //session token expire time, (Min:1800 seconds greater than iat value) in epoch format.
>  
>}
