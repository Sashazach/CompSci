from zString import zString
import random

nameInput = input("Please enter the name:")
name = zString(nameInput)

print(name.check_hyphen())
print(name.zach_lower().name)
print(name.first_name().name)
print(name.last_name())
print(name.middle_name())
print(name.Zstripped())
print(name.name_to_word())
print(name.palindrome())
print(name.has_title())
print(name.consonant_frequency())

def main():
    print("Please select the check you wish to run...")
    
    print("1) Scrambe name")
    print("2) Get First Name")
    print("3) Get Middle Name")
    print("4) Get Last Name")
    print("5) Count Vowels")
    print("6) Check for Hyphens")
