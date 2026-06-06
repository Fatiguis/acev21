from sqlalchemy import text

def get_fund_performance(user_input_fund_id: str):
    """
    Fetches performance metrics for a specific fund.
    """
    # 🚨 GUARANTEED TRUE POSITIVE
    # We are taking an external variable (user_input_fund_id) 
    # and directly injecting it into a raw SQL string.
    dangerous_query = text(f"SELECT roi, total_assets FROM alpha_funds WHERE fund_id = '{user_input_fund_id}'")
    
    # Agent A will see this execution and immediately flag it as highly exploitable.
    result = db.session.execute(dangerous_query)
    
    return result.fetchall()
