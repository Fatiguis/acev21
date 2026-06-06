import json
import base64
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/api/v1/process-config")
def process_config(config_b64: str):
    """
    Accepts a base64 encoded JSON string from the user, decodes it, 
    and safely parses it with `json.loads()`.
    
    JSON deserialization does not execute arbitrary code, avoiding the
    insecure deserialization vulnerability associated with `pickle`.
    """
    
    # 1. THE SOURCE: The input comes directly from the user.
    try:
        config_bytes = base64.b64decode(config_b64)
        
        # 2. THE SINK: `json.loads` safely parses text data without executing code.
        config_data = json.loads(config_bytes)
        
        return {"status": "success", "data": config_data}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid config payload")
