def main():
    while True:
        print("\nChoose a function to execute:")
        print("1: Factorial")
        print("2: Summation")
        print("3: Powers")
        print("4: Sum of Digits")
        print("5: Fibonacci")
        print("6: Product of Digits")
        print("7: Product of Two Numbers")
        print("8: Sum of Numbers in Range")
        print("q: Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            n = int(input("Enter a number for factorial: "))
            print("Factorial:", factorial(n))
        elif choice == '2':
            n = int(input("Enter a number for summation: "))
            print("Summation:", summation(n))
        elif choice == '3':
            a = int(input("Enter the base number: "))
            n = int(input("Enter the exponent: "))
            print("Powers:", powers(a, n))
        elif choice == '4':
            n = int(input("Enter a number to find the sum of its digits: "))
            print("Sum of Digits:", sum_of_digits(n))
        elif choice == '5':
            n = int(input("Enter an index for the Fibonacci sequence: "))
            print("Fibonacci:", fibonacci(n))
        elif choice == '6':
            n = int(input("Enter a number to find the product of its digits: "))
            print("Product of Digits:", product_of_digits(n))
        elif choice == '7':
            x = int(input("Enter the first number: "))
            y = int(input("Enter the second number: "))
            print("Product of Two Numbers:", product(x, y))
        elif choice == '8':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            print("Sum of Numbers in Range:", sum(start, end))
        elif choice.lower() == 'q':
            print("Bye!")
            break
        else:
            print("Invalid choice, please try again!")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def summation(n):
    if n == 0:
        return n
    else:
        return n + summation(n-1)

def powers(a, n):
    if n == 0:
        return 1
    return a * powers(a, n-1)

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return sum_of_digits(n // 10) + n % 10

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def product_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    else:
        return (n % 10) * product_of_digits(n // 10)

def product(x, y):
    return x * y

def sum(start, end):
    if start > end:
        return 0
    else:
        return start + sum(start + 1, end)  

if __name__ == "__main__":
    main()
