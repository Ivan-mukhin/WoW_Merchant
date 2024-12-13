import loginCreds 
import requests
import localServer


def get_auth_code(id, redirectUri, authUrl):
    # Startup local server to catch auth code
    localServer.callback()

    auth_req_url = ('https://oauth.battle.net/authorize'
            '?response_type=code'
            '&scope=openid'
            '&state=AbCdEfG'
            f'&redirect_uri={redirectUri}'
            f'&client_id={id}')

    print(f"Auth app: {auth_req_url}")

    # TODO: program an automatic catcher for the auth code  
    
    authCode = input("Enter the authorization code from the URL: ")
    return authCode


id = loginCreds.getID()
secret = loginCreds.getSecret()
redirectUri = 'http://localhost:8080/callback'
authUrl = 'https://oauth.battle.net/authorize'

get_auth_code(id, redirectUri, authUrl)