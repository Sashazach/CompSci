import os
import matplotlib.pyplot as plt
import csv

def main():
    file_input = open(r"C:\Users\zbostock26\Desktop\student_data_2023.csv")

    writer = csv.writer(file_input)
        
    file_input.readline()                       #skip first line of header info
    answer = "Y"
    go = True
   
 
    while go is True:
        print("1) Print All Student in Grade 12")
        print("2) lookup particular person")
        print("3) Plot Number of People Per Grade")
        
        answer = input("Enter Choice or 'Q' to quit:")

        if answer == "1":
            check_seniors(file_input)
        elif answer == "2":
            lookupPerson(file_input)
        elif answer == "3":
            boys_and_girls(file_input)
        elif answer.upper() == "Q":
            go = False
            print("Program Done Running")
            return
           
def lookupPerson(file_in):
    
    file_in.seek(1)
    
    first_name = input("Enter First Name:")
    last_name = input("Enter Last Name:")
    os.system('cls')

    for record in file_in:
        kid = record.split(",")
        if kid[1].lower() == first_name.lower() and kid[0].lower() == last_name.lower():
            line1 = f"NAME-{kid[1]} {kid[0]}\tPOSITION IN SCHOOL-{kid[2]} \n"
            line2 = f"GENDER: {kid[3]}\tADRESS-{kid[4]} {kid[5]} {kid[6]}\n"
            
            print(line1 + line2, end="")

def boys_and_girls(file_in):
    file_in.seek(1)                                   

    gradeData = {
        "nursery": 0,
        "pre-k": 0,
        "kindergarten": 0,
        "grade 1": 0,
        "grade 2": 0,
        "grade 3": 0,
        "grade 4": 0,
        "grade 5": 0,
        "grade 6": 0,
        "grade 7": 0,
        "grade 8": 0,
        "grade 9": 0,
        "grade 10": 0,
        "grade 11": 0,
        "grade 12": 0
    }
    
    for record in file_in:
        kid = record.split(",")
        if (kid[3]).lower() != "current grade": 
            gradeData[(kid[3]).lower()] += 1
    
    for key in gradeData:
        print(key + ": " + str(gradeData[key]), end=" ")
    
    print("\n")
    
def check_seniors(file_in):    
    file_in.seek(1)                                    

    for record in file_in:
        kid = record.split(",")
        if kid[2] == "Grade 12":
            print(kid[1] + " " + kid[0])    

if __name__ == '__main__':
    main()