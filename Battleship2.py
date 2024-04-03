import random
import copy
import os
import time

def main():
    print("What mode would you like?")
    print("1) Player Vs. AI")
    print("2) Player Vs. Player")
    
    choice = input("Enter your selection:")

    if choice == "1":
        pass

def ai_turn():
    pass

def initiate_empty_grid():
    grid = []
    for i in range(9):
        grid.append([])
        for j in range(9):
            grid[i].append("#")
    
    return grid

def get_input():
    while True:
        adress = input("Enter Collumn and Row (Horizontal, Vertical):")
            
        try:
            coll, row = [int(integer) for integer in adress.split(",")]
            if coll != None and 0 <= coll <= 8 and 0 <= row <= 8:
                return row - 1, coll - 1
            else: 
                raise()
        except:
            os.system('cls')
            print("\nInput error, try again...\n")

def mark_tile(coords, grid, marking):
    markings = {'sea':'#', 'ship':'\b◽' }
    
    grid[0][1] = markings[marking]

def place_ships_manually(grid):
    ships = {'aircraft carrier':5, 'destroyer':3, 'submarine':2}
    
    print("Admiral! Position your ships for battle!\n")
    print("(Hint: Use the arrow keys to move ship and R to rotate.\nPress enter to confirm ship placement!)")
    for i in range(1, 6):
        print("Admiral, here is a map of the sea!\n")
        print('\n'.join(['   '.join([str(cell) for cell in row]) for row in grid]))
        print(f"Position your aircraft carrier! ({i}/5)")
        
        rotation = 0
        tiles = []
        for ship, length in ships.items():
            for i in range(2, length):
                mark_tile((4,i), grid, 'ship')
            print('\n'.join(['   '.join([str(cell) for cell in row]) for row in grid]))
            
            while True:
                move = input()
                time.sleep(0.2)
            
place_ships_manually(initiate_empty_grid())