# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# SSetta,6.13.2026,Created Script
# ------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
from data_classes import Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []
        self.employee_type = Employee

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2026-01-02", "ReviewRating": 1},
            {"FirstName": "Alice", "LastName": "Smith", "ReviewDate": "2026-01-10", "ReviewRating": 3},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_employee_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data, self.employee_type)

        # Assert that the employee_data list contains the expected student objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[1].review_date, "2026-01-10")
        self.assertEqual(self.employee_data[1].review_rating, 3)


if __name__ == "__main__":
    unittest.main()
