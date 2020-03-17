# City, Country - Unittest, TestCase

# import unittest
# from city_functions import get_city_country_name

# class CityTestCase(unittest.TestCase):

#     def test_city_country(self):
#         city_country = get_city_country_name('santiago', 'chile')
#         self.assertEqual(city_country, 'Santiago, Chile')

# if __name__ == '__main__':
#     unittest.main()



# Population - Unittest, TestCase

import unittest
from city_functions import get_city_country_name

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        city_country = get_city_country_name('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country = get_city_country_name('santiago', 'chile', 5000000)
        self.assertEqual(city_country, 'Santiago, Chile - population 5000000.')


if __name__ == '__main__':
    unittest.main()