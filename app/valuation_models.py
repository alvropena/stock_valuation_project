class ValuationModel:
    def discounted_cash_flow(self, cash_flows, discount_rate, growth_rate, years=5):
        present_value = 0
        for year in range(1, years + 1):
            cash_flow = cash_flows[year - 1] * (1 + growth_rate) ** year
            present_value += cash_flow / (1 + discount_rate) ** year
        return present_value
    
    def price_to_earnings(self, earnings, price):
        if earnings > 0:
            return price / earnings
        return None
