import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.vijay = Employee('vijay', 'sethupathi', 70000)
    
    def test_give_default_raise(self):
        self.vijay.give_raise()
        self.assertEqual(self.vijay.salary, 75000)

    def test_give_custom_raise(self):
        self.vijay.give_raise(10000)
        self.assertEqual(self.vijay.salary, 80000)

unittest.main()