import random

# Initialize deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] #creates the classes of the 4 types of cards
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'] # creates the values that a card may have
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11} # creates a dictionary that assigns each string value in "ranks" an integer value

# Functions
def deal_card(): # defines the deal_card function with no parameters
    suit = random.choice(suits) # sets the suit variable to a random choice in the "suits" list
    rank = random.choice(ranks) # creates a string value to represent the value of the card
    return (rank, suit) # returns the selected rank and suit and closes the function

def calculate_hand_value(hand): # defines the calculate_hand_value function with the parameter hand
    value = sum([values[card[0]] for card in hand]) # sums the values of the cards in the hand using dictionary and index 0 (the int value)
    num_aces = sum([1 for card in hand if card[0] == 'Ace']) # checks if the card stirng value in values dictionary is an ace
    
    while value > 21 and num_aces: #if the value is less than 21 and there are aces do the following
        value -= 10 # subtracts the value by 10 
        num_aces -= 1 # subtracts the number of aces by 1 so this doesn't call again
    
    return value # returns the value of the deck

# Game setup
player_hand = [deal_card(), deal_card()] # deals two cards to the player at the start of the game
dealer_hand = [deal_card(), deal_card()] # deals two cards to the dealer at the start of the game

# Game loop
while True:
    player_value = calculate_hand_value(player_hand) # calculates the value of the player hand
    dealer_value = calculate_hand_value(dealer_hand) # calculates the value of the dealer hand
    
    print("\nYour hand:", player_hand, "Value:", player_value) # prints the value of the player hand as well as the cards
    print("Dealer's hand:", [dealer_hand[0], 'Hidden']) # prints the name of the first car in the dealer's deck
    
    if player_value == 21: #  if the player's value is 21, the player wins
        print("Blackjack! You win!")
        break
    elif player_value > 21: # if the player's value is greater than 21, the player busts
        print("Bust! You lose.")
        break
    
    action = input("Do you want to 'hit' or 'stand'? ").lower() # asks if the player wants to hit or stand
    
    if action == 'hit': # checks what the input of action was
        player_hand.append(deal_card()) # deals another car to the player
    elif action == 'stand': # stops drawing player cards
        while dealer_value < 17: # if the dealer value is less than 17
            dealer_hand.append(deal_card()) # deals another card to the dealer
            dealer_value = calculate_hand_value(dealer_hand) # calculates the new dealer hand's value
        
        print("Dealer's hand:", dealer_hand, "Value:", dealer_value) # prints the cards in dealer hand and the value of those cards
        
        if dealer_value > 21 or player_value > dealer_value:# if the dealer value is greater than 21 or the player value is still greater than the dealer value
            print("You win!") # prints "You win"
        elif dealer_value > player_value: # if the dealer value is greater than the player value
            print("Dealer wins.") # prints "Dealer wins"
        else: # if those above conditions are not met
            print("It's a tie!") # prints "It's a tie!"
        
        break # breaks the loop