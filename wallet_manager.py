def connect_to_external_services():
    """
    🚨 REAL-WORLD VULNERABILITY: Hardcoded Secrets
    Let's see if Semgrep catches a realistic-looking key that doesn't end in 'EXAMPLE'.
    """
    
    # 1. A structurally valid (but fake) AWS Master Key
    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    
    # 2. A structurally valid (but fake) Slack Webhook
    SLACK_ALERTS = os.environ["SLACK_ALERTS"]
    
    return True
