## Author - Zachry Bostock
## Date Completed - 12/16/23
## Implemented Project Componenets (as listed on course website) - 1, 2, 3, 4, 5, 6, 7, 8, 9a, 10a, 10
## Bugs - N/A
## Challenges - N/A

## Import required libraries 
import os
import io
from pathlib import Path

## selection_map is a key for converting user input from get_user_selected_data into indexes for the CSV file
selection_map = {
    1:4,
    2:6,
    3:7,
    4:8
}

def main():
    """
    Description - A main function to drive the program.
    Takes - N/A
    Does - Processing for relative file path and opens file in addition to calling functions based on user input
    Returns - N/A
    """

    try:
        current_dir = Path(__file__).parent
        file_path = current_dir / "student_data_2023.csv"
        file_input = open(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        
    file_input.readline()                     
    answer = "Y"
    go = True
   
    while go is True:
        print("1) Print All Student in Grade 12")
        print("2) Lookup student in database")
        print("3) Make selections from data")
        print("4) Append data row to CSV")

        answer = input("Enter Choice or 'Q' to quit:")

        if answer == "1":
            check_seniors(file_input)
        elif answer == "2":
            lookup_person(file_input)
        elif answer == "3":
            get_user_selected_data(file_input)
        elif answer == "4": 
            append_to_csv(file_path)
        elif answer.upper() == "Q":
            go = False
            print("Program Done Running")
            return
        
def print_student_data(data):
    """
    Description - A function to print data in an organized fashion.
    Takes - data (A data row from the CSV in the form of a list)
    Does - Prints the information for the relevant row in a way easy for the user to understand.
    Returns - N/A
    """

    labels = ["First Name", "Middle Name", "Last Name", "Grade", "Advisor Last", "Advisor First", "City", "State", "Zipcode"]
    for label, value in zip(labels, data):
        if "Advisor" in label:
            value = value.replace('"', '').strip()
        print(f"{label.ljust(15)}: {value}")

def lookup_person(file_in):
    """
    Description - A function to find a specific person in the CSV file.
    Takes - file_in (A CSV file.)
    Does - Takes user input for first and last names and finds the first person in the CSV file with matching names.
    Returns - N/A
    """
    file_in.seek(1)
    
    first_name = input("Enter First Name:")
    last_name = input("Enter Last Name:")

    os.system('cls')

    for record in file_in:
        kid = record.split(",")
        if kid[0].lower() == first_name.lower() and kid[2].lower() == last_name.lower():
            print_student_data(kid)
            while True:
                new_file = input("Would you like to create a CSV file with this data? (Y/N):")
                if new_file.lower() == "n":
                    break
                elif new_file.lower() == "y":
                    while True:
                        file_name = input("Enter the name of the new file (Hint: end it with .csv):")
                        lists_to_csv(file_name, [kid])
                        break
                else:
                    print("Invalid input, please re-enter.") 
            return 
        
    print("No match found \n\n")



def lists_to_csv(file_path, data):
    headers = ["First Name", "Middle Name", "Last Name", "Grade", "Advisor Last", "Advisor First", "City", "State", "Zipcode"]

    print(data)
    with open(file_path, 'w') as file:
        file.write(','.join(headers) + '\n')
        
        for row in data:
            if row[4] == "None":
                row.insert(5, "None")
                
            csv_row = ','.join(row).replace('"', '').replace(", ", ',')
            
            file.write(csv_row + '\n')
            
    print("Your new file has been sucessfully created!")

def append_to_csv(file_path):
    """
    Description - append_to_csv appends data to the CSV file in use.
    Takes - file_path (The relative path to the file in use.)
    Does - Takes user input and then combines the inputs into a list before writing that list into the file as a data row.
    Returns - N/A
    """
    first_name = input("Enter First Name:")
    middle_name = input("Enter Middle Name:")
    last_name = input("Enter Last Name:")
    grade = input("Enter Grade:")
    advisor_last = input("Enter Advisor Last Name:")
    advisor_first = input("Enter Advisor First Name:")
    city = input("Enter City:")
    state = input("Enter State:")
    zipcode = input("Enter Zipcode:")

    data = [first_name, middle_name, last_name, grade, advisor_last, advisor_first, city, state, zipcode]

    data = [str(item) for item in data]

    with open(file_path, 'a') as file:
        file.write(','.join(data) + '\n')

def get_selections(index, selection, iterable):
    """
    Description - get_selections is a helper function for the get_user_selected_data function. 

    Takes - Index (A value representing the index of the column in the CSV specified by the user in get_user_selected_data)
    selection (The value specified for the column of the CSV to which the user has specified in get_user_selected_data)
    iterable (Either a list or a IO_File depending on how get_selections is called)

    Does - Processes the students that have the specified value in the specified column of the CSV and adds them to the selection_list. 
    Returns - the selection_list of all the students that met the specification of the user.

    """

    if isinstance(iterable, io.IOBase):
        iterable.seek(1)
        os.system('cls')

    selection_list = []

    row = -1
    for record in iterable:
        row += 1

        if row >= 1:
            if isinstance(iterable, io.IOBase):
                kid = record.split(",")
            else:
                kid = record

            ## 1 is subtracted from the index for people without advisors because there is a comma included between the first and last advisor names, 
            ## which potentially skews aspects of the analysis if not handled 
            if index == 8:
                if kid[4] == "None":
                    if str(kid[index - 1]).strip("\n") == selection.lstrip('0'):
                        selection_list.append(kid)
                else:
                    if str(kid[index]).strip("\n") == selection.lstrip('0'):
                        selection_list.append(kid)
            elif index == 7:
                if kid[4] == "None":
                    if kid[index - 1].lower() == selection.lower():
                        selection_list.append(kid) 
                else:
                    if kid[index].lower() == selection.lower():
                        selection_list.append(kid) 
            elif index == 6:
                if kid[4] == "None":
                    if kid[index - 1].lower() == selection.lower():
                        selection_list.append(kid) 
                else:
                    if kid[index].lower() == selection.lower():
                        selection_list.append(kid) 
            elif index == 4:
                if kid[index].replace('"', '').lower() == selection.lower():
                    selection_list.append(kid)

    return selection_list

def get_user_selected_data(file_in):
    """
    Description - get_user_selected_data presents users with a menu from which they may choose what selections to make of the entire CSV file. As more selections are added, the number of 
    people in the selection group shrinks. The user has the option of writing the output to a CSV.
    Takes - file_in (The current file in use)
    Does - Gets user input to determine a specified column and respective value to check the CSV for. Uses the helper function get_selections to fetch the users in the specified catagory. 
    Returns - N/A
    """
    requirement_number = 1
    filtered_students = []
    stop = "n"

    print("Select Data For Retrieval...\n")

    while True:
        print("1) Advisor Last Name")
        print("2) Town")
        print("3) State (Abreviation Required)")
        print("4) Zipcode")


        parameter = input(f"Select search parameter {requirement_number}:")
        if parameter.isnumeric() and 0 < int(parameter) <= 4:
                requirement_number += 1
                parameter_selection = input("Enter what this search parameter should be:")

                if requirement_number == 2:
                    filtered_students = get_selections(selection_map[int(parameter)], parameter_selection, file_in)
                else: 
                    filtered_students = get_selections(selection_map[int(parameter)], parameter_selection, filtered_students)

                if len(filtered_students) == 0:
                    os.system('cls')
                    print("No matches found")
                    return 
                else:
                    while stop != "y":
                        print(f"{len(filtered_students)} students meet your current criteria.")
                        stop = input("Get Students Matching Criteria Now (Y/N)")
                        if stop.lower() == "y" or stop.lower() == "n":
                            break
                        else:
                            print("Invalid input, please re-enter")
                    if stop.lower() == "n":
                        continue
                    else:
                        for student in filtered_students:
                            print_student_data(student)
                        while True:
                            new_file = input("Would you like to create a CSV file with this data? (Y/N):")
                            if new_file.lower() == "n":
                                break
                            elif new_file.lower() == "y":
                                while True:
                                    file_name = input("Enter the name of the new file (Hint: end it with .csv):")
                                    lists_to_csv(file_name, filtered_students)
                                    break
                            else:
                                print("Invalid input, please re-enter.")
                    print("\n")
        else:
            print("Invalid input, please re-enter")
            os.system('cls')    

def check_seniors(file_in):    
    """
    Description - check_seniors searches for and prints to the user all seniors at GCDS and their associated data in the CSV file. Allows users to write output to a new CSV file.
    Takes - file_in (The current in use file)
    Does - Uses a for loop to create a list of all seniors in the data. 
    Returns - N/A
    """


    file_in.seek(1)                                    

    seniors = []

    for record in file_in:
        kid = record.split(",")
        if kid[3] == "Grade 12":
            print_student_data(kid) 
            seniors.append(kid)

    while True:
        new_file = input("Would you like to create a CSV file with this data? (Y/N):")
        if new_file.lower() == "n":
            break
        elif new_file.lower() == "y":
            while True:
                file_name = input("Enter the name of the new file (Hint: end it with .csv):")
                lists_to_csv(file_name, seniors)
                break
        else:
            print("Invalid input, please re-enter.") 

if __name__ == '__main__':
    main()