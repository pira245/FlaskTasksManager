"""
    This is a basic source for a python function testing based on Unittest framework.
    The file run various test on a file called company where the tested functions are stored.
"""

# Import Libraries:
import unittest
# Import file source file for test:
from MyUnittest.core_package.Company import get_country


# Create a class for a TestCase
class TestLibraryCompany(unittest.TestCase):
    # Test for the function: get_country
    # Allow country test: means the iso code is the get_country list.
    def test_allow_country(self):
        iso_code_list = ['DK', 'UK', 'SE', 'NO', 'BJ']
        for iso_code in iso_code_list:
            country = get_country(iso_code=iso_code)
            self.assertEqual(True, country[0])
            self.assertEqual(dict, type(country[1]))

    # Disallow country test: means the iso code is not in the get_country list.
    def test_disallow_country(self):
        country = get_country(iso_code='DA')
        self.assertEqual(False, country[0])
        self.assertEqual(None, (country[1]))

    # TypeError test: means check iso_code type to be a string.
    def test_raise_country_TypeError(self):
        with self.assertRaises(TypeError):
            get_country()
            get_country(iso_code=12)

    # ValueError test: means check iso_code value to be 2 characters long.
    def test_raise_country_ValueError(self):
        with self.assertRaises(ValueError):
            get_country(iso_code='Denmark')
            get_country(iso_code='D')
            get_country(iso_code='')


if __name__ == '__main__':
    unittest.main()
