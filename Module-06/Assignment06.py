# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   SSetta,5/26/2026,Created Script
# ------------------------------------------------------------------------------------------ #

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog:
    SSetta,5.26.2026,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads data from a JSON file

        ChangeLog:
        SSetta,5.26.2026,Created function

        :return: list with the student data
        """
        file = None

        # Extract the data from the file
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except Exception as e:
            IO.output_error_messages("Please check that the file exists and that it is in a json format.", e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes data to a JSON file

        ChangeLog:
        SSetta,5.26.2026,Created function

        :return: None
        """
        file = None

        try:
            file = open(file_name, "w")
            json.dump(students, file, indent=2)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with writing to the file.", e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog:
    SSetta,5.26.2026,Created Class
    SSetta,5.26.2026,Added menu output and input functions
    SSetta,5.26.2026,Added a function to display the data
    SSetta,5.26.2026,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays the error message if one is encountered

        ChangeLog:
        SSetta,5.25.2026,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu of choices to the user

        ChangeLog:
        SSetta,5.26.2026,Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """
        This function gets a menu choice from the user

        ChangeLog:
        SSetta,5.26.2026,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Choose a menu option: ")
            if choice not in ("1", "2", "3", "4"): # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__(),e)
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function prints student course registration

        ChangeLog:
        SSetta,5.25.2026,Created function

        :return: None
        """
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function takes student input for student name and course name

        ChangeLog:
        SSetta,5.25.2026,Created function

        :return: list of student data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")
            student_entry = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student_entry)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            IO.output_error_messages(print(e),e)
        except Exception as e:
            IO.output_error_messages("Error: There was a problem with your entered data.", e)
        return(student_data)

# import modules
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        print("The following data was saved to file:")
        IO.output_student_courses(student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
