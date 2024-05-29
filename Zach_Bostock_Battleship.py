"""
## Author - Zachry Bostock
## Date Completed - 12/16/23
## Implemented Project Componenets (as listed on course website) - ALL
## Bugs - N/A
## Bonus - 1

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
import os

os.system('cls')

def generate_radar(board):
    #takes -- board: the AI_board that is used to generate the player radar
    #processes -- the radar to show the player based on the board arg
    #returns -- radar: the player's radar
    conversion_dict = {'S':'#', '#':'#', 'X':'H', 'M':'M'}

    radar = []
    for i in range(len(board)):
        radar.append([])
        for j in range(len(board)):
            radar[i].insert(j, conversion_dict[board[i][j]])
    
    return radar

def computer_move(player_grid):
    #takes -- player_grid: the grid of the player
    #processes -- handles the computer guessing and updating of player_grid accordingly
    #returns -- player_grid: the player's new grid
    while True:
        row, coll = random.randint(0, 7), random.randint(0, 7)
        print(player_grid[coll][row])
        if player_grid[coll][row] == 'S':
            player_grid[coll][row] = 'X'
            return player_grid
        elif player_grid[coll][row] == '#':
            player_grid[coll][row] = 'M'
            return player_grid
        
def game_loop(player_grid, computer_grid):
    #takes -- player_grid: the grid of the player, computer_grid: the grid of thed computer
    #processes -- the main game logic after the ships have been placed
    #returns -- NONE
    while True:
        computer_grid = player_move(player_grid, computer_grid)
        
        if check_game_status(computer_grid):
            print("Game Over, you win!")
            return
        player_grid = computer_move(player_grid)
        if check_game_status(player_grid):
            print("Game Over, you lost!")
            return
    
def player_move(player_grid, computer_grid):
    #takes -- player_grid: the grid of the player, computer_grid: the grid of the computer
    #processes -- handles logic for player guessing, including both printing the player's radar and board and collecting and validating input
    #returns -- computer_grid: the computer's grid updated following the player's guess
    conversion_dict = {'S':'X', '#':'M'}

    radar = generate_radar(computer_grid)
    os.system('cls')

    while True:
        print("Admiral, its time to engage the enemy fleet! \nMake a move!\n\nHere is our most updated Radar!\n")
        print('\n'.join(['   '.join([str(cell) for cell in row]) for row in radar]))
        print('\nHere is your grid!\n')
        print('\n'.join(['   '.join([str(cell) for cell in row]) for row in player_grid]))
        
        coll, row = get_input([radar, player_grid])
        
        os.system('cls')
        
        try:
            computer_grid[coll][row] = conversion_dict[computer_grid[coll][row]]
            return computer_grid

        except:
            if KeyError:
                print("Tile already guessed!")
    
def initiate_empty_grid():
    #takes -- NONE
    #processes -- initiates and appends to a 2d array using for loop iteration to create an 8x8 grid
    #returns -- grid: an empty 8x8 2d array
    grid = []
    for i in range(8):
        grid.append([])
        for j in range(8):
            grid[i].append("#")

    return grid

def main():
    #takes -- NONE
    #processes -- logic for setting up boards
    #returns -- NONE
    ai_grid = auto_place_ships(initiate_empty_grid())
    
    player_grid = manual_place_ships(initiate_empty_grid())
    
    game_loop(player_grid, ai_grid)

def get_tile(request):
    #purpose -- to allow for easier customization of symbols. Provides high level accessibility, making it easier to modify graphics
    #takes -- request: the requested tile type
    #processes -- matches the tile request string to a symbol
    #returns -- returns the requested symbol
    tiles = {'ship':'S', 'sea':'#'}
    return tiles[request]
    
def auto_place_ships(board):
    #takes -- board: an empty 8x8 2d array
    #processes -- fetches coordinates for ships from the create_ship_coords() function to place onto board randomly. Ensures valid ship placement.
    #returns -- board: an 8x8 2d array populated with ships
    ship_types = {'aircraft carrier':5, 'destroyer':3, 'submarine':2, 'patrol boat':1}

    for ship, length in ship_types.items():
        new_ship_coords = create_ship_coords(board, length)[0]
        for coord in new_ship_coords:
            board[coord[0]][coord[1]] = get_tile('ship')
    return board
    
def check_coord_valididity(coords, board, eraser_key = None):
    #takes -- coords: a tuple representing the comprised of the collumn and row of a position respectively. Board: the 8x8 2d array to check the coord validity against. 
        #eraser_key: a list containing tiles that would be erased given the other coords not in eraser_key are valid (function ignores these coords in calculation)
    #processes -- checks the validity of the coord entered given the board and eraser key args
    #returns -- a boolean representing whether the cords are valid (true) or invalid (false)
    for coord in coords:
        if not ((-1 < coord[0] < 8) and (-1 < coord[1] < 8)):
            return False
    for coord in coords:
        if eraser_key != None and coord not in eraser_key and board[coord[0]][coord[1]] == get_tile('ship'):
            return False
    return True

def create_ship_coords(board, length):
    #takes -- board: an 8x8 2d array. length: the length of the board
    #processes -- creates a set of coordiantes, either vertical or horizontal, represented by a list
    #returns -- coords: the set of coords represented as a list. rotated: the status of the ships rotation
    while True:
        coords = []
        rotated = False
        if random.randint(0, 2) == 1:
            coll = random.randint(0, 7  - length) #horizontal
            row = random.randint(0, 7) #vertical
        else:
            rotated = True
            coll = random.randint(0, 7) #horizontal
            row = random.randint(0, 7 - length) #vertical

        for i in range(length):
            if rotated == False:
                coords.append([row, coll + i])
            else:
                coords.append([row + i, coll])
        if check_coord_valididity(coords, board) == True:
            return coords, rotated


def get_input(boards=None):
    #takes -- boards: a boolean variable defining whether or not boards have been setup yet
    #processes -- uses a while loop to get a selected row, coll from a user. Ensures they are valid before proceeding with logic
    #returns -- row-1: the valid row coordinate. coll-1: the valid collumn coordinate
    while True:
        adress = input("Enter Collumn and Row (Horizontal, Vertical):")
            
        try:
            coll, row = [int(integer) for integer in adress.split(",")]
            if (coll != None and row != None) and 0 < coll <= 8 and 0 < row <= 8:
                return row - 1, coll - 1
            else: raise()
        except:
            os.system('cls')
            print("\nInput error, try again...\n")

            if boards != None:
                print("Admiral, its time to engage the enemy fleet! \nMake a move!\n\nHere is our most updated Radar!\n")
                print('\n'.join(['   '.join([str(cell) for cell in row]) for row in boards[0]]))
                print('\nHere is your grid!\n')
                print('\n'.join(['   '.join([str(cell) for cell in row]) for row in boards[1]]))

def move_ship(ship, board, direction, rotated):
    #takes -- ship: a list representing the coordinates of the ship being moved. board: an 8x8 2d array. direction: the direction the user should move, a string representing a WASD key
    #processes -- the direction the user would like to move in, and proceeds to execute logic to move the ship while ensuring the new position is valid
    #returns -- board: the board with the updated ship position. ship: the new coordinates of the ship on the board
    eraser_key = []
    for i in range(len(ship)):
        eraser_key.append([ship[i][0], ship[i][1]])
        
    if direction.upper() == "W":
        for i in range(len(ship)):
            ship[i][0] -= 1
                
    elif direction.upper() == "S":
        for i in range(len(ship)):
            ship[i][0] += 1
            
    elif direction.upper() == "D":
        for i in range(len(ship)):
            ship[i][1] += 1
            
    elif direction.upper() == "A":
        for i in range(len(ship)):
            ship[i][1] -= 1


    if check_coord_valididity(ship, board, eraser_key) == True:
        for coord in eraser_key:
            board[coord[0]][coord[1]] = get_tile('sea')
        for coordinate in ship:
            board[coordinate[0]][coordinate[1]] = get_tile('ship')#switch this
    else:
        ship = eraser_key

    return board, ship

def manual_place_ships(board):
    #takes -- board: an 8x8 2d array
    #processes -- allows the user to use the WASD keys to manuver 1 of each shiptype found in the ship_types dictionary
    #returns -- board: the original 8x8 2d array populated with four ships, one of each class
    ship_types = {'aircraft carrier':5, 'destroyer':3, 'submarine':2, 'patrol boat':1}
    
    i = 0
    for ship, length in ship_types.items():
        ship = []
        i += 1
                
        new_ship_coords, rotated = create_ship_coords(board, length)
        for coord in new_ship_coords:
            board[coord[0]][coord[1]] = get_tile('ship')
            ship.append(coord)

        while True:
            print('Use WASD to manuver your ship!')
            print(f'Input (P) to place ({i}/4)\n')
            print('\n'.join(['   '.join([str(cell) for cell in row]) for row in board]))

            direction = input("Enter Input: ")
            os.system('cls')
            if direction.upper() == "P":
                break
            board, ship = move_ship(ship, board, direction, rotated)

    return board

def check_game_status(grid):
    #takes -- grid- a 2d array containg the tiles and their status as occupied or unoccupied
    #does -- iterates over the grid using nested for loops to determine if their are any occupied squares on the board
    #returns -- "running" if there are alive ships on the board, returns "Over" if there are no more alive ships on the board
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                print(i, j)
                return False
    return True

main()