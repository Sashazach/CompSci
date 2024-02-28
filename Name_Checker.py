import random
from zString import zString

vowel_counter = 0
    
nameInput = input("Please enter the name:")
name = zString(nameInput)

print(name.check_hyphen())
print(name.zach_lower())
print(name.first_name())

def main():
    

    
    print("Please select the check you wish to run...")
    
    print("1) Scrambe name")
    print("2) Get First Name")
    print("3) Get Middle Name")
    print("4) Get Last Name")
    print("5) Count Vowels")
    print("6) Check for Hyphens")


