"""Testing the functionality of Coffee Shop Game"""
import unittest
from coffee_shop_simulator import CoffeeShopSimulator

class CoffeeShopSimTest(unittest.TestCase):
    """test functionality"""
    floats = [
        "3.64",
        "3",
        "3.9",
        "7.8"
    ]
    def test_convert_to_float(self):
        """Test string conversion to float"""
        for dec in self.floats:
            self.assertEqual(CoffeeShopSimulator.convert_to_float(dec), float(dec))

    def test_x_to_y(self):
        """Test that x_of_y returns a list of x copies of the number y"""
        number_list = [1, 1, 1, 1, 1]
        self.assertEqual(CoffeeShopSimulator.x_of_y(5, 1), number_list)

    def test_x_of_y_strings(self):
        """Test the returns x_of_y with a list of string elements"""
        string_list = ["A", "A", "A", "A", "A"]
        self.assertEqual(CoffeeShopSimulator.x_of_y(5, "A"), string_list)
    # to act as self in testing
    test = CoffeeShopSimulator()
    
    def test_increment_day(self):
        self.assertEqual(CoffeeShopSimulator.increment_day(self.test), 2)

if __name__ == '__main__':
    unittest.main()
