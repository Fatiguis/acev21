from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

class WebhookPayload(BaseModel):
    target_url: str
    event_data: dict

@router.post("/api/webhooks/dispatch")
def dispatch_webhook(payload: WebhookPayload):
    """
    Dispatches a user-configured webhook.
    
    🚨 REAL-WORLD VULNERABILITY: Cloud Metadata SSRF
    We are taking a user-supplied URL (payload.target_url) and making an HTTP request 
    to it without checking if the URL points to an internal network address.
    
    An attacker can bypass the internet and pass:
    "target_url": "http://169.254.169.254/latest/meta-data/iam/security-credentials/"
    
    Because the server itself is executing the request, AWS will trust it and return 
    the server's cloud infrastructure passwords directly to the attacker.
    """
    
    # 1. THE SOURCE: target_url comes directly from the API payload (untrusted input)
    url = payload.target_url
    
    try:
        # 2. THE SINK: The untrusted input is executed by the requests library.
        # Semgrep's taint analysis will catch this because the path from Source to Sink is unbroken.
        response = requests.post(url, json=payload.event_data, timeout=5)
        
        # Returning the response body makes this a "Full SSRF" (much more dangerous than a Blind SSRF)
        return {
            "status": "success", 
            "status_code": response.status_code,
            "response_body": response.text[:200] 
        }
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Webhook failed: {e}")
        raise HTTPException(status_code=400, detail="Webhook dispatch failed")
