"""
--algo--

main()
    1) call function to initialize and then return AI and Player grids
    2) call function to allow player to place ships
        a) For loop with 5 iterations
            1. tell user to place ships (#/#)
            2. put ship down on center of board and print it for player
            3. allow player to manuver ship with main cardinal directions using a move_ship function that takes ship coords as a list
                a. check if player input is valid and not hitting another ship
                b. update the board to reflect movement
    3) call function to auto-place ships on AI board
    4) call main game loop, passing AI and player boards
        a) call function to collor boards
        b) print boards and allow user input for shooting
        c) update boards with valid user input
        d) check both boards for game over scenario
"""

import random
import copy
import os

def get_input(board=None):
    while True:
        adress = input("Enter Collumn and Row (Horizontal, Vertical):")
            
        try:
            coll, row = [int(integer) for integer in adress.split(",")]
            if (coll != None and row != None) and 0 < coll <= 8 and 0 < row <= 8:
                return row - 1, coll - 1
            else: 
                raise()
        except:
            os.system('cls')
            print("\nInput error, try again...\n")

            if board != None:
                print('\n'.join(['   '.join([str(cell) for cell in row]) for row in board]))


def manual_place_ships(grid):
    ship_classes = []
    ship_stats = []
    
    for i in range(1, 6):
        print('\n'.join(['   '.join([str(cell) for cell in row]) for row in grid]))
        print(f"\nEnter where would you like to place your ship ({i}/5):")
                
        row, coll = get_input(board=grid)
        
        grid[row][coll] = "S"

    return grid

def check_game_status(grid):
    #takes -- grid- a 2d array containg the tiles and their status as occupied or unoccupied
    #does -- iterates over the grid using nested for loops to determine if their are any occupied squares on the board
    #returns -- "running" if there are alive ships on the board, returns "Over" if there are no more alive ships on the board
    for i in range(8):
        for j in range(8):
            if grid[i][j] == 1:
                return "Running"
    return "Over"
