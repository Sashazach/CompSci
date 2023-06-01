import time
import os

def make_float(type = "number"):
    while True:
        num = input(f"Enter {type}: ")
        
        try:
            return float(num)
        except:
            print("Invalid")
def exponent():
    base = make_float(type = "exponent")
    exponent = make_float(type = "base")
    print(f"Answer:{base ** exponent}")
def add():
    num1 = make_float()
    num2 = make_float()
    return num1 + num2
def subtract():
    num1 = make_float()
    num2 = make_float()
    return num1 - num2
def multiply():
    num1 = make_float()
    num2 = make_float()
    return (num1 * num2)
def divide():
    num1 = make_float()
    while True:
        num2 = make_float()
        
        if num2 == 0:
            print("cannot divide by zero")
        else:
            return (num1 / num2)
    
def sum(numbers):
    sum_numbers = []
    current_sum = 0
    num1 = make_float()
    sum_numbers.append(num1)
    while True:
        num2 = make_float()
        sum_numbers.append(num2)
        sum_or_not = input(f"{type1}: Y/N")
        if sum_or_not.upper() == "Y":
            if type1 == "Sum":
                for index in range(len(sum_numbers)):
                    current_sum += sum_numbers[index]
                return current_sum
                break
            elif type1 == "Max":
                current_max = 0
                for index in range(len(sum_numbers)):
                    if sum_numbers[index] > current_max:
                        current_max = sum_numbers[index]
                return current_max
                break
            else:
                print("Invalid")
            
valid_options = [add, subtract, multiply, divide, sum, exponent, max]

def main():
    while True:
        operation = input("Operation: \n     1. add \n     2. subtract \n     3. multiply \n     4. divide \n     5. sum \n     6. exponent \n     7. Max \n     8. Quit \n(1, 2, 3, 4, 5, 6, 7, 8):")
        if operation == "1" or operation == "2" or operation == "3" or operation == "4" or operation == "5" or operation == "6" or operation == "7":
            if valid_options[int(operation) - 1] == sum:
                answer = sum("Sum")
            elif valid_options[int(operation) - 1] == max:
                answer = sum("Max")
            else:    
                answer = valid_options[int(operation) - 1]()
            os.system('cls')
            print(f"Answer:{answer}")
            time.sleep(2)
            os.system('cls')
        elif operation == "8":
            break
        
main()