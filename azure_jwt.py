import msal
import requests
import os
import base64
import urllib3

def mailsend():
# Disable SSL certificate verification
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize the MSAL confidential client
client_id = "d0bbbce0-984d-4ca1-b2e2-a1e3bdb24e86"
client_secret = 'H1y8Q~bJuo7MOxe6ONLneKBKACK5nq7hi4Ivpaxm'
authority = "https://login.microsoftonline.com/e3ff91d8-34c8-4b15-a0b4-18910a6ac575"

app = msal.ConfidentialClientApplication(
    client_id,
    authority=authority,
    client_credential=client_secret,
)

# Define the scopes
scopes = ["https://graph.microsoft.com/.default"]

# Acquire token
result = None
result = app.acquire_token_silent(scopes, account=None)

if not result:
    result = app.acquire_token_for_client(scopes)

if "access_token" in result:
    print(result["access_token"])
