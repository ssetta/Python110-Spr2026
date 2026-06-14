# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Create an application
# # Description: A collection of classes to present employee info
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# SSetta,6.13.2026,Edited Script
# ------------------------------------------------------------------------------------------------- #

# import modules
from data_classes import FILE_NAME, MENU, employees, menu_choice, Employee
from processing_classes import FileProcessor
from presentation_classes import IO

# Beginning of the main body of this script
try:
    employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)
except FileNotFoundError as e:
    IO.output_error_messages(e)
except Exception as e:
    IO.output_error_messages(e)

# Repeat the following tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)  # Note this is the class name (ignore the warning)
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
