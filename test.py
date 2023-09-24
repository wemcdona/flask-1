from unittest import TestCase
from app import is_valid_currency, convert_currency

class AppTestCase(TestCase):
    def test_is_valid_currency(self):
        self.assertTrue(is_valid_currency('AAA'), 'Invalid currency code!')
        self.assertTrue(is_valid_currency('USD'))

    def test_convert_currency(self):
        self.assertEqual(convert_currency('USD', 'EUR', 20), 18.754901)
        self.assertNotEqual(convert_currency('USD', 'JPY', 50), 80)