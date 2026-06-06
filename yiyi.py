from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/network-test")
def test_network():
    """
    🚨 VULNERABILITY: Command Injection
    """
    # 1. THE SOURCE: We are taking input directly from the web URL
    target_ip = request.args.get("ip")
    
    # 2. THE SINK: We are stuffing that web input directly into a server shell command
    # An attacker could send: ?ip=8.8.8.8; cat /etc/passwd
    # This would execute the ping, and then print the server's passwords.
    command = f"ping -c 1 {target_ip}"
    
    # Semgrep will 100% catch this because it sees the data flowing from the web to the system.
    os.system(command)
    
    return "Test complete!"
