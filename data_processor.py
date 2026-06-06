import pickle
import base64
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/api/v1/process-config")
def process_config(config_b64: str):
    """
    🚨 REAL-WORLD VULNERABILITY: Insecure Deserialization
    We are accepting a base64 encoded string from the user, decoding it, 
    and passing it directly into `pickle.loads()`.
    
    An attacker can generate a malicious pickle payload that, when loaded, 
    executes arbitrary system commands (like `rm -rf /` or a reverse shell).
    """
    
    # 1. THE SOURCE: The input comes directly from the user.
    try:
        config_bytes = base64.b64decode(config_b64)
        
        # 2. THE SINK: `pickle.loads` is unsafe. It executes whatever is in the bytes.
        # Semgrep's p/python rules identify `pickle.loads` as a critical security risk.
        config_data = pickle.loads(config_bytes)
        
        return {"status": "success", "data": config_data}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid config payload")
