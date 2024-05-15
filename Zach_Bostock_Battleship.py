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

os.system('cls')

def color_board(board):
    conversion_dict = {'S':'H', '#':'#'}
    pass

def generate_radar(board):
    conversion_dict = {'S':'#', '#':'#', 'X':'H', 'M':'M'}

    radar = []
    for i in range(len(board)):
        radar.append([])
        for j in range(len(board)):
            radar[i].insert(j, conversion_dict[board[i][j]])
    
    return radar

def computer_move(player_grid):
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
        else:
            radar = generate_radar(computer_grid)
    
def initiate_empty_grid():
    grid = []
    for i in range(8):
        grid.append([])
        for j in range(8):
            grid[i].append("#")

    return grid

def main():
    ai_grid = auto_place_ships(initiate_empty_grid())
    
    player_grid = manual_place_ships(initiate_empty_grid())
    
    result = game_loop(player_grid, ai_grid)

def get_tile(request):
    tiles = {'ship':'S', 'sea':'#'}
    return tiles[request]
    
def auto_place_ships(board):
    ship_types = {'aircraft carrier':5, 'destroyer':3, 'submarine':2, 'patrol boat':1}

    for ship, length in ship_types.items():
        new_ship_coords = create_ship_coords(board, length)[0]
        for coord in new_ship_coords:
            board[coord[0]][coord[1]] = get_tile('ship')
    return board
    
def check_coord_valididity(coords, board, eraser_key = None):
    for coord in coords:
        if not ((-1 < coord[0] < 8) and (-1 < coord[1] < 8)):
            return False
    for coord in coords:
        if eraser_key != None and coord not in eraser_key and board[coord[0]][coord[1]] == get_tile('ship'):
            return False
    return True

def create_ship_coords(board, length):
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

            if boards != None:
                print("Admiral, its time to engage the enemy fleet! \nMake a move!\n\nHere is our most updated Radar!\n")
                print('\n'.join(['   '.join([str(cell) for cell in row]) for row in boards[0]]))
                print('\nHere is your grid!\n')
                print('\n'.join(['   '.join([str(cell) for cell in row]) for row in boards[1]]))

def move_ship(ship, board, direction, rotated):
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