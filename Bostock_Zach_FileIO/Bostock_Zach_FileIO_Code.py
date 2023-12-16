import os
import matplotlib.pyplot as plt
import csv
import io

selection_map = {
    1:4,
    2:6,
    3:7,
    4:8
}

def main():
    file_input = open(r"C:\Users\Zach\Documents\student_data_2023.csv")

    writer = csv.writer(file_input)
        
    file_input.readline()                       #skip first line of header info
    answer = "Y"
    go = True
   
 
    while go is True:
        print("1) Print All Student in Grade 12")
        print("2) Lookup student in database")
        print("3) Make selections from data")
        
        answer = input("Enter Choice or 'Q' to quit:")

        if answer == "1":
            check_seniors(file_input)
        elif answer == "2":
            lookup_person(file_input)
        elif answer == "3":
            get_user_selected_data(file_input)
        elif answer == "4": 
            
        elif answer.upper() == "Q":
            go = False
            print("Program Done Running")
            return
        
def print_student_data(data):
    labels = ["First Name", "Middle Name", "Last Name", "Grade", "Advisor Last", "Advisor First", "City", "State", "Zipcode"]
    for label, value in zip(labels, data):
        if "Advisor" in label:
            value = value.replace('"', '').strip()
        print(f"{label.ljust(15)}: {value}")

def lookup_person(file_in):
    
    file_in.seek(1)
    
    first_name = input("Enter First Name:")
    last_name = input("Enter Last Name:")

    os.system('cls')

    for record in file_in:
        kid = record.split(",")
        if kid[0].lower() == first_name.lower() and kid[2].lower() == last_name.lower():
            print_student_data(kid)
            return 
        
    print("No match found \n\n")

def get_selections(index, selection, iterable):
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

def append_to_csv(file_in, data):
    data = [str(item) for item in data]

    with open(file_in, 'a') as file:
        file.write(','.join(data) + '\n')

def get_user_selected_data(file_in):
    requirement_number = 1
    filtered_students = []
    stop = "n"

    print("Select Data For Retrieval...\n")

    while True:
        print("1) Advisor Last Name")
        print("2) Town")
        print("3) State")
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
                            print("Invalid, please re-enter selection")
                    if stop.lower() == "n":
                        continue
                    else:
                        for student in filtered_students:
                            print_student_data(student)
                            
                    print("\n")
        else:
            print("Invalid Input")
            os.system('cls')    

def check_seniors(file_in):    
    file_in.seek(1)                                    

    for record in file_in:
        kid = record.split(",")
        if kid[3] == "Grade 12":
            print(kid[0] + " " + kid[1] + " " + kid[2])    

if __name__ == '__main__':
    main()