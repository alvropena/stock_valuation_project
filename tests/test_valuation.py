import unittest
from app.valuation_models import ValuationModel

class TestValuationModel(unittest.TestCase):
    def setUp(self):
        self.model = ValuationModel()

    def test_dcf(self):
        cash_flows = [50000, 52000, 54000, 56000, 58000]
        discount_rate = 0.1
        growth_rate = 0.05
        result = self.model.discounted_cash_flow(cash_flows, discount_rate, growth_rate)
        self.assertTrue(result > 0)

if __name__ == '__main__':
    unittest.main()
