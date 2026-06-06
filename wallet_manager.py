def get_cloud_database_connection():
    """
    🚨 REAL-WORLD VULNERABILITY: Hardcoded Secrets
    Committing live API keys or AWS credentials directly into source code.
    If this repository is ever made public, or if an employee's laptop is compromised, 
    the attacker gets instant, unrestricted access to the company's cloud infrastructure.
    """
    
    # Semgrep's p/secrets rule will instantly flag the 'AKIA' pattern 
    # as a high-severity leaked Amazon Web Services key.
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    return connect_to_aws(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

def connect_to_aws(key, secret):
    # Dummy function so the code runs
    return "Connected!"
