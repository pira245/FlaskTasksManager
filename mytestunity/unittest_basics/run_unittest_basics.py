import unittest
import sys

sys.path.append('unittest_basics/')


def test_all():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir='.', pattern='Test*.py'))
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


# Test related with the python class student
def test_Student():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    # add tests to the test suite
    suite.addTests(loader.discover(start_dir='.', pattern='Test*Student.py'))
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


if __name__ == "__main__":
    # Run all test available
    # test_all()
    # Run only the test related with the python class student
    test_Student()
    # unittest.main()
