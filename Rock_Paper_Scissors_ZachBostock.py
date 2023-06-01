round = 0 # sets round to 0
ScoreTracker = {} # initalizes the scoretracker dict
scoreLine = {} # initalizes the scorline dict
import random # imports the random function
import os # imports operating system function
from pprint import pprint ## imports pprint from pprint in python library

Stopping = False # initializes Stopping as a boolean and sets it to false

player2Score = 0 # sets player2Score to 0
player1Score = 0 # Sets player1Score to 0

computerChoices = ["R", "P", "S"]  # sets the computerChoices list to the values inside []

while True:
    useComputer = input("Would you like to play against a computer? Y/N") # asks for user input with prompt inside ("")
    if useComputer.upper() == "Y": # checks if the uppercase version of the input is equal to "Y"
        playMode = "Computer" # Sets playMode variable equal to "Computer"
        break
    elif useComputer.upper() == "N": # checks if the uppercase version of the input is equal to "N"
        playMode = "Multiplayer" # Sets playMode to "Multiplayer"
        break
    elif useComputer != "Y" or "N": # Else if the input is not equal to "Y" or "N"
            print("Please enter valid input") # Asks for valid input
        
def newRound(): ## begins defining the newRound function
    global round # this line imports a variable to the function
    global scoreLine # this line imports a variable to the function
    global player2Score  # this line imports a variable to the function
    global player1Score  # this line imports a variable to the function
        
    round += 1
    
    Player1Won = (F"Round {round} Player1Won") # defines the Player1Won to the given F strng
    Player2Won = (F"Round {round} Player2Won") # defines the Player1Won to the given F string
    
    print("A new round has begun!") # prints the text inside the ("") to the terminal
    player1Choice1 = input("Player1, what would you like to play? Please answer with R/P/S:") # sets the variable player1Choice1 to the input to the printed message
    player1Choice = player1Choice1.upper() # sets player1Choice to the player1Choice but uppercase
    os.system('cls') # clears the output
    if playMode == "Computer": #if the playermode variable is equal to "Computer"
        player2Choice = random.choice(computerChoices) #sets player@choice to a random choice from the computerChoices list
        if player2Choice.upper() == "P": # converts the computer's choice to the full text word
            player2ChoicePrint = "Paper" # converts the computer's choice to the full text word
        elif player2Choice.upper() == "R": # converts the computer's choice to the full text word
            player2ChoicePrint = "Rock" # converts the computer's choice to the full text word
        elif player2Choice.upper() == "S": # converts the computer's choice to the full text word
            player2ChoicePrint = "Scissors" # converts the computer's choice to the full text word
        print(f"The computer has played {player2ChoicePrint}") # prints the full text word to the output in an F string
    else:
        player2Choice1 = input("Player2, what would you like to play? Please answer with R/P/S:") #sets player2Choice1 to the input from the ("") that the user gives
        player2Choice = player2Choice1.upper() # sets player2Choice to the uppercase version of the player2Choice1 variable
    if player1Choice == player2Choice: # Checks for draw
        print("The round is drawn") # prints "The round is drawn" to the user
        newRound() # begins new round
    if player1Choice != "R" and player1Choice != "P" and player1Choice != "S": #check for invalid inputs from player1
        print("Pleaes enter either R, P or S!") #asks for valid input in terminal via print
        newRound() # calls newRound function, a new round starts
    elif player2Choice != "R" and player2Choice != "P" and player2Choice != "S": # checks of invalid inputs from player2
        print("Pleaes enter either R, P or S!") # asks for valid input from  player2
        newRound() # begins new round
    elif player1Choice == "R" and player2Choice == "P" or player1Choice == "P" and player2Choice == "R": # checks if the inputs are rock and paper 
        if player2Choice == "P": # checks if Player2 was the one to play the winning move
            ScoreTracker[round] = Player2Won # inserts new key value into ScoreTracker as a string
            if playMode == "Multiplayer": # checks if the Playmode is multiplayer 
                print("player 2 won") # prints that "player 2 won"
            else: # else playmode has to be Computer
                print("The computer won") # prints that the computer won
            player2Score += 1 # adds a point to player2's score
        elif player2Choice == "R": # else it has to be player1
            ScoreTracker[round] = Player1Won # adds a new value into ScoreTracker as a string
            
            print("player 1 won") # prints "player 1 won"
            
            player1Score += 1 # 1 point is added to player1Score
    elif player1Choice == "R" and player2Choice == "S" or player1Choice == "S" and player2Choice == "R": # checks if the inputs are S and R
        if player2Choice == "R": # checks if player2 played the winning move
            ScoreTracker[round] = Player2Won # adds a key value as a string to the dict ScoreTracker
            if playMode == "Multiplayer": # checks if playMode is equal to Multiplayer
                print("player 2 won") # prints to terminal that player 2 won
            else: # else the game must be in Computer playmode
                print("The computer won") # prints that the computer won to the output
            player2Score += 1 # adds 1 to player2Score
        else: # player1Won must have just played the winning move
            ScoreTracker[round] = Player1Won # adds a new valye to the ScoreTracker dict, a string
            print("player 1 won") # prints that "player 1 won" to the output
            player1Score += 1 # adds 1 to player1Score
    elif player1Choice == "S" and player2Choice == "P" or player1Choice == "P" and player2Choice == "S": # checks ifthe inputs are P and S
        if player2Choice == "S": # checks if player2 played the winning move
            ScoreTracker[round] = Player2Won # adds a new value to the dict to say that Player2Won the round that the game is on
            if playMode == "Multiplayer": # checks if the playMode is "Multiplayer"
                print("player 2 won") # prints text to the terminal
            else: # else the computer must be playing
                print("The computer won") # prints that the computer won
            player2Score += 1 # adds 1 to player2Score
        else: # else, player 1 must have won
            ScoreTracker[round] = Player1Won # adds a new value to the ScoreTracker dict, the Player1Won string
            print("player 1 won") # prints that "player 1 won"
            player1Score += 1 # adds 1 point to player1Score
    while True: # enters while true to ensure valid inputs
        seeResults = input("Round complete, see past round results? Y/N Input STOP to end program:") # sets the seeResults variable to the input given after the text is printed to the terminal
        if seeResults.upper() == "Y":  # if see results 
            scoreLine["Current Scoreline"] = (F"Player 1's score is {player1Score} and Player 2's score is {player2Score}") # sets the scoreLine string with current variables in an F strng
            pprint(scoreLine) # pretty prints the ScoreLine 
            pprint(F"Round History: {ScoreTracker}") # pretty prints the ScoreTracker in an F string
            Again = input("Would you like to play another round? Y/N") # sets the variable "Again" to the input given when the text inside the ("") is printed to the user
            if Again.upper() == "Y": # If the Again variable in its uppercase form is "Y"
                newRound() # begins new round by calling function
            elif Again.upper() == "N": # if the uppercase form is "N"
                Stopping = True # sets Stopping boolean to True
                print("Program has ended") # prints the "Program has ended"
                break # breaks so the program can end
        elif seeResults.upper() == "STOP":
            Stopping = True # sets the stopping boolean to True
            print("Program has now ended") # prints that the program has ended
            break # breaks the loop so the program can end
        elif seeResults.upper() == "N": # checks if the seeResults uppercase version is equal to "N"
            Again = input("Would you like to play another round? Y/N") # asks if the user wants to play another round and sets input equal to the Again variable
            if Again.upper() == "Y": # sets the Again variable to its uppercase form and then checks if it is equal to "Y"
                newRound() # begins new round by calling newRound function
            elif Again.upper() == "N": # checks if the uppercase version of the Again variable is equal to "N"
                Stopping = True # sets stopping boolean equal to True
                print("Program has ended") # prints that the program has ended
                break # breaks the loop so the program can end
            else: # if none of the above conditions are met (if the input is invalid)
                print("Please enter valid inputs") # asks for a valid input and repeats the input loop (while loop)
        else:
            print("Please enter a valid input below:") # prints the message in the ("")
if Stopping == False: # checks if the Stopping boolean is equal to False
    newRound() # begins new roud by calling the newRound function

            
        
            
    
    
            
        
    
    
    
    