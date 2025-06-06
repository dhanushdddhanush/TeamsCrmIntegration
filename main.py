# main.py
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from zoho_service import initiate_zoho_auth, handle_zoho_callback, get_zoho_leads, create_zoho_lead
from salesforce_service import initiate_salesforce_auth, handle_salesforce_callback, get_salesforce_leads, create_salesforce_lead
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# ZOHO ROUTES
@app.get("/zoho/auth/initiate")
def zoho_auth():
    return RedirectResponse(initiate_zoho_auth())

@app.get("/zoho/auth/callback")
def zoho_callback(code: str):
    return handle_zoho_callback(code)

@app.get("/zoho/get-leads")
def get_leads():
    return get_zoho_leads()

@app.post("/zoho/create-lead")
def post_lead(payload: dict):
    return create_zoho_lead(payload)

# SALESFORCE ROUTES
@app.get("/salesforce/auth/initiate")
def salesforce_auth():
    return RedirectResponse(initiate_salesforce_auth())

@app.get("/salesforce/auth/callback")
def salesforce_callback(code: str):
    return handle_salesforce_callback(code)

@app.get("/salesforce/get-leads")
def sf_get_leads():
    return get_salesforce_leads()

@app.post("/salesforce/create-lead")
def sf_create_lead(payload: dict):
    return create_salesforce_lead(payload)
