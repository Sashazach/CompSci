from What_In_Name.zString import zString

## Author - Zachry Bostock
## Date Completed - 2/29/2024
## Implemented Project Components (as listed on the course website) - range(0, 12) + 15
## Bugs - N/A

def main():
    """
    Description - A function to take user input
    Takes - None
    Does - Performs the operation.
    Returns - Describe the return value.
    """
    nameInput = input("Please enter the name:")
    name = zString(nameInput)

    while True:
        print("Please select the check you wish to run...")
        
        print("1) Check For Hyphens")
        print("2) Get Lowercase")
        print("3) Get Uperrcase")
        print("4) Get First Name")
        print("5) Get Last Name")
        print("6) Get Middle Name")
        print("7) Get Pailindrome")
        print("8) Check for Title")
        print("9) Get Consonant Frequency Data")
        print("10) Get Number of vowels")
        print("11) Get Reversed Name")

        selection = input("Enter Function to Run:")

        if selection == "1": print(name.check_hyphen())
        elif selection == "2": print(name.zach_lower().name)
        elif selection == "3": print(name.zach_upper().name)
        elif selection == "4": print(name.first_name())
        elif selection == "5": print(name.last_name())
        elif selection == "6": print(name.middle_name())
        elif selection == "7": print(name.palindrome())
        elif selection == "8": print(name.has_title())
        elif selection == "9": print(name.consonant_frequency())
        elif selection == "10": print(name.count_vowels())
        elif selection == "11": print(name.reverse_name().name)

        else: print("Invalid input, try again")
main()
