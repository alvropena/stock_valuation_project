import argparse
from app.endpoints import FinancialEndpoints

def main():
    parser = argparse.ArgumentParser(description="Financial Data CLI")
    
    parser.add_argument("command", choices=[
        "income_statements", "balance_sheets", "cash_flow_statements", 
        "company_facts", "insider_transactions", "prices", "price_snapshot", "filings"
    ], help="The API endpoint to call")

    # Add query params if needed
    parser.add_argument("--ticker", help="The stock ticker symbol (e.g., AAPL, NVDA)")
    parser.add_argument("--period", default="annual", choices=["annual", "quarterly", "ttm"], help="Period (default: annual)")
    parser.add_argument("--limit", type=int, default=30, help="Limit the number of results (default: 30)")

    args = parser.parse_args()
    financial_endpoints = FinancialEndpoints()

    if args.command == "income_statements":
        result = financial_endpoints.get_income_statements(args.ticker, args.period, args.limit)
    elif args.command == "balance_sheets":
        result = financial_endpoints.get_balance_sheets(args.ticker, args.period, args.limit)
    elif args.command == "cash_flow_statements":
        result = financial_endpoints.get_cash_flow_statements(args.ticker, args.period, args.limit)
    elif args.command == "company_facts":
        result = financial_endpoints.get_company_facts()
    elif args.command == "insider_transactions":
        result = financial_endpoints.get_insider_transactions()
    elif args.command == "prices":
        result = financial_endpoints.get_prices(args.ticker)
    elif args.command == "price_snapshot":
        result = financial_endpoints.get_price_snapshot(args.ticker)
    elif args.command == "filings":
        result = financial_endpoints.get_filings(args.ticker)
    
    print(result)

if __name__ == "__main__":
    main()
