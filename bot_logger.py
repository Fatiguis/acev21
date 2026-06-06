import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/api/v1/bots/arbitrage/logs/download")
def download_bot_log(log_filename: str):
    """
    🚨 REAL-WORLD VULNERABILITY: Path Traversal (Directory Traversal)
    We are taking a user-supplied filename and blindly appending it to our log directory path.
    
    An attacker can bypass the intended folder by using dot-dot-slash notation:
    ?log_filename=../../../../../etc/passwd
    OR
    ?log_filename=../../../../../app/.env
    
    The server will happily navigate up the directory tree, read the hidden passwords, 
    and serve them directly to the attacker's browser.
    """
    
    # 1. THE SOURCE: The untrusted input comes directly from the URL parameter.
    base_dir = "/var/log/trading_bots/active_runs/"
    
    # 2. THE SINK: os.path.join does NOT protect against '../'. 
    # If log_filename is "../../etc/passwd", file_path becomes exactly that.
    file_path = os.path.join(base_dir, log_filename)
    
    # The server checks if the file exists and then blindly serves it.
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Log file not found")
        
    return FileResponse(file_path)
