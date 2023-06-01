#Creator: Zach Bostock, Sources: Ms. Marciano, W3Schools, Date lsat edited: March 1st 2023, Bugs: none
#Purpose: To function as an 8-ball to inputs given




import random 

responses = ["You now have bad luck", "Everything is fine", "The world will catch on fire soon", "You will have great luck for the rest of today"] # creates list

while True: # Begins while true loop
    userQuestion = input("Hello- I'm a magic 8-ball, ask a question: (Enter stop to end program)") #Sets userQuestion variable equal to the input given to the text in () that is printed
    if (userQuestion.upper() == "STOP"): # If the upper case translation of the userQuestion variable is equal to STOP then the if statement will be executed
        break # Loop is broken
    
    print(random.choice(responses)) #Prints a random slot from the responses list
print("File has ended") # prints to user that the file has ended
    
    
    

