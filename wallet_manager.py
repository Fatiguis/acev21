def connect_to_external_services():
    """
    🚨 REAL-WORLD VULNERABILITY: Hardcoded Secrets
    Let's see if Semgrep catches a realistic-looking key that doesn't end in 'EXAMPLE'.
    """
    
    # 1. A structurally valid (but fake) AWS Master Key
    AWS_ACCESS_KEY_ID = "AKIA5F3B1G7H9J2K4L6M"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCY1234567890"
    
    # 2. A structurally valid (but fake) Slack Webhook
    SLACK_ALERTS = "https://hooks.slack.com/services/T12345678/B12345678/a1b2c3d4e5f6g7h8i9j0k1l2"
    
    return True
