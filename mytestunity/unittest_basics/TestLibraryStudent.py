"""
    This is a basic source file for a python class testing based on Unittest framework.
    The file run various test on a file called student where the tested class is stored.

    Usage of:
    - setUp()
    - tearDown()
    - setUpClass()
    - tearDownClass()
"""

# Import Libraries:
import unittest
# Import file source file for test:
from wema4unittest.Library.Student import Student
from datetime import timedelta
from unittest.mock import patch


# TestCase Class for unittest testing
class TestStudent(unittest.TestCase):
    # Class Fixture
    @classmethod
    def setUpClass(cls):
        print("set up class")

    def setUp(self):
        print("setup")
        self.student = Student("John", "Doe")

    # Class Fixture
    @classmethod
    def tearDownClass(cls):
        print("tear down Class")

    def tearDown(self):
        print("tear down")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

        """
        The method below is also great!  But keep in mid that  it will
        only be correct if a student has received 1 extenstion.  If
        they receive a second - it would return false
        self.student.apply_extension(5)
        
        self.assertEqual(self.student.end_date, self.student._start_date + timedelta(days=370))
        """

    def test_course_schedule_success(self):
        with patch("wema4unittest.Library.Student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        """
        In the path "student" comes from the name of the file student.py
        If you have named the file something else - it will need to match
        eg, students.py would need "students.requests.get"
        """
        with patch("wema4unittest.Library.Student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")


if __name__ == "__main__":
    unittest.main()
