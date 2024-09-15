from app.api_client import APIClient

class FinancialEndpoints:
    def __init__(self):
        self.api_client = APIClient()

    def get_income_statements(self, ticker, period='annual', limit=30):
        """Fetch income statements."""
        endpoint = '/financials/income-statements'
        params = {"ticker": ticker, "period": period, "limit": limit}
        return self.api_client.make_request(endpoint, params)

    def get_balance_sheets(self, ticker, period='annual', limit=30):
        """Fetch balance sheets."""
        endpoint = '/financials/balance-sheets'
        params = {"ticker": ticker, "period": period, "limit": limit}
        return self.api_client.make_request(endpoint, params)

    def get_cash_flow_statements(self, ticker, period='annual', limit=30):
        """Fetch cash flow statements."""
        endpoint = '/financials/cash-flow-statements'
        params = {"ticker": ticker, "period": period, "limit": limit}
        return self.api_client.make_request(endpoint, params)

    def get_company_facts(self):
        """Fetch company facts (no query parameters)."""
        endpoint = '/company/facts'
        return self.api_client.make_request(endpoint)

    def get_insider_transactions(self):
        """Fetch insider transactions (no query parameters)."""
        endpoint = '/insider-transactions'
        return self.api_client.make_request(endpoint)

    def get_prices(self, ticker):
        """Fetch prices."""
        endpoint = '/prices'
        params = {"ticker": ticker}
        return self.api_client.make_request(endpoint, params)

    def get_price_snapshot(self, ticker):
        """Fetch price snapshot."""
        endpoint = '/prices/snapshot'
        params = {"ticker": ticker}
        return self.api_client.make_request(endpoint, params)

    def get_filings(self, ticker):
        """Fetch filings."""
        endpoint = '/filings'
        params = {"ticker": ticker}
        return self.api_client.make_request(endpoint, params)
