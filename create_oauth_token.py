import requests
import os
from dotenv import load_dotenv


# https://developer.ups.com/api/reference?loc=en_US#tag/OAuth-Client-Credentials

def get_oath_token():
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    url = "https://wwwcie.ups.com/security/v1/oauth/token"

    payload = {
        "grant_type": "client_credentials"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "x-merchant-id": "string"
    }

    response = requests.post(url, data=payload, headers=headers,
                             auth=(client_id, client_secret))
    if response.status_code != 200:
        exit()
    data = response.json()
    return data['access_token']
