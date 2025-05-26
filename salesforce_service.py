# salesforce_service.py
import requests
import os
from dotenv import load_dotenv
load_dotenv()


# CONFIG
SF_CLIENT_ID = os.getenv("SF_CLIENT_ID")
SF_CLIENT_SECRET = os.getenv("SF_CLIENT_SECRET")
SF_REDIRECT_URI = "http://localhost:8000/salesforce/auth/callback"
SF_REFRESH_TOKEN = os.getenv("SF_REFRESH_TOKEN")
TOKEN_URL = "https://login.salesforce.com/services/oauth2/token"
API_BASE = "https://your_instance.salesforce.com/services/data/v52.0/sobjects"

access_token = None
instance_url = None

def initiate_salesforce_auth():
    return (
        f"https://login.salesforce.com/services/oauth2/authorize"
        f"?response_type=code&client_id={SF_CLIENT_ID}"
        f"&redirect_uri={SF_REDIRECT_URI}"
    )

def handle_salesforce_callback(code):
    global access_token, instance_url
    res = requests.post(
        TOKEN_URL,
        data={
            "grant_type": "authorization_code",
            "code": code,
            "client_id": SF_CLIENT_ID,
            "client_secret": SF_CLIENT_SECRET,
            "redirect_uri": SF_REDIRECT_URI,
        },
    )
    data = res.json()
    access_token = data.get("access_token")
    instance_url = data.get("instance_url")
    return data

def get_salesforce_leads():
    headers = {"Authorization": f"Bearer {access_token}"}
    res = requests.get(f"{instance_url}/services/data/v52.0/query?q=SELECT+Id,+FirstName,+LastName,+Company+FROM+Lead", headers=headers)
    return res.json()

def create_salesforce_lead(payload):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    res = requests.post(f"{instance_url}/services/data/v52.0/sobjects/Lead/", headers=headers, json=payload)
    return res.json()
    

