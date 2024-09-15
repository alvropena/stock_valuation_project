from app.api_client import APIClient
from app.valuation_models import ValuationModel

def run_valuation(ticker):
    api_client = APIClient()
    
    # Fetch data
    income_statements = api_client.fetch_financial_data("income_statements", ticker)
    cash_flows = api_client.fetch_financial_data("cash_flow_statements", ticker)

    # Extract cash flow data
    cash_flow_data = [statement['net_income'] for statement in cash_flows['cash_flow_statements']]

    # Perform DCF valuation
    model = ValuationModel()
    stock_value = model.discounted_cash_flow(cash_flow_data, discount_rate=0.1, growth_rate=0.05)
    
    return {"ticker": ticker, "value": stock_value}
