import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_country = city_country('santigo', 'chile')
        self.assertEqual(formatted_country, 'Santigo, Chile')
    
    def test_city_country(self):
        formatted_country = city_country('santigo', 'chile', population=400000)
        self.assertEqual(formatted_country, 'Santigo, Chile - population 400000')

if __name__ == '__main__':
    unittest.main()