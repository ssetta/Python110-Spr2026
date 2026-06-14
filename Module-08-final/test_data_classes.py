# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# SSetta,6.13.2026,Edited Script
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee

import os
import sys

print("cwd:", os.getcwd())
print("test file:", __file__)
print("sys.path[0:5]:", sys.path[0:5])

class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")


class TestEmployee(unittest.TestCase):

    def test_Employee_init(self):  # Tests the constructor
        employee = Employee("Alice", "Smith", "2026-02-01", 4)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, "2026-02-01")
        self.assertEqual(employee.review_rating, 4)

    def test_employee_review_date_type(self):  # Test the date validation
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "invalid_date",4)
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "26-02-01", 4)
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "4", 4)

    def test_employee_review_rating_type(self):
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "2026-02-01", 100)
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "2026-02-01", "invalid_rating")
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "2026-02-01", "100")


    def test_employee_str(self):
        student = Employee("Eve", "Brown", "2026-02-01",4)  # Tests the __str__() magic method
        self.assertEqual(str(student), "Eve,Brown,2026-02-01,4")

if __name__ == '__main__':
    unittest.main()