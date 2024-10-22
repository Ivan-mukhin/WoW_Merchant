# File for authorizin


import requests
from requests.auth import HTTPBasicAuth

# Step 1: Get Authorization Code
def get_authorization_code(client_id, redirect_uri, authorization_url):
    auth_request_url = (
        f"{authorization_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope=read"
    )
    print(f"Visit this URL to authorize the application: {auth_request_url}")
    # The user will visit this URL, and the authorization server will redirect to the redirect_uri with a code in the URL.
    authorization_code = input("Enter the authorization code from the URL: ")
    return authorization_code

# Step 2: Exchange Authorization Code for Access Token
def get_access_token(client_id, client_secret, authorization_code, redirect_uri, token_url):
    payload = {
        'grant_type': 'authorization_code',
        'code': authorization_code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    
    response = requests.post(token_url, data=payload)
    
    if response.status_code == 200:
        token_json = response.json()
        access_token = token_json.get("access_token")
        return access_token
    else:
        print(f"Failed to get access token: {response.status_code}")
        print(response.text)
        return None

# Step 3: Make API Requests using the Access Token
def make_api_request(access_token, api_endpoint):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.get(api_endpoint, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"API request failed with status {response.status_code}")
        return None

# Example usage
client_id = "your_client_id"
client_secret = "your_client_secret"
redirect_uri = "https://yourapp.com/callback"
authorization_url = "https://authorization-server.com/oauth/authorize"
token_url = "https://authorization-server.com/oauth/token"
api_endpoint = "https://api-server.com/data"

# Get authorization code from the user (first step of OAuth 2.0 flow)
authorization_code = get_authorization_code(client_id, redirect_uri, authorization_url)

# Exchange the authorization code for an access token
access_token = get_access_token(client_id, client_secret, authorization_code, redirect_uri, token_url)

# Use the access token to make authorized API requests
if access_token:
    api_response = make_api_request(access_token, api_endpoint)
    if api_response:
        print(api_response)
