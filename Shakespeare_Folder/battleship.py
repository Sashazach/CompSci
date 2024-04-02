import random
import copy
import os
import time

def check_game_status(grid):
    for i in range(8):
        for j in range(8):
            if grid[i][j] == 1:
                return "Running"
    return "Over"

def check_hit(grid, row, coll):
    if grid[coll][row] == 1:
        return "Hit!"
    else:
        return "Miss!"

def start_game_loop(game_mode):
    ##make Player Grid
    player_grid = manual_place_ships(initiate_empty_grid())
    os.system('cls')
    print("Grid Created! Here it is...")
    
    print('\n'.join(['   '.join([str(cell) for cell in row]) for row in player_grid]))

    if game_mode == "1":
        ##generate AI grid
        backend_ai_grid = auto_place_ships(initiate_empty_grid())
    while True: 
        time.sleep(2)
        player_grid, backend_ai_grid = ai_turn(backend_ai_grid,  player_grid)
        
        if check_game_status(backend_ai_grid) == "Over":
            print("Game Over!")
            break
        
        backend_ai_grid = player_turn(backend_ai_grid, player_grid)
        
        if check_game_status(backend_ai_grid) == "Over":
            print("Game Over!")
            break
        
def ai_turn(backend_ai_grid, player_grid):
    while True:
        coll = random.randint(0, 7)
        row = random.randint(0, 7)

        if backend_ai_grid[coll][row] != "M" and player_grid[coll][row] != "D":
            if player_grid[coll][row] == "S":
                player_grid[coll][row] = "X"
                print("One of your ships has been hit!\n")
                ##print('\n'.join(['   '.join([str(cell) for cell in row]) for row in player_grid]))
                break
            else:
                player_grid[coll][row] = "M"
                print("The computer missed!")
                backend_ai_grid[coll][row] = "M"
                break
    return player_grid, backend_ai_grid

def player_turn(backend_ai_grid, playergrid):
    row, coll = get_input()
        
    hit = check_hit(backend_ai_grid, row, coll)
    print(hit)
    if hit == "Hit!":
        backend_ai_grid[coll][row] = "D"
    else:
        backend_ai_grid[coll][row] = 2

    frontend_ai_grid = copy.deepcopy(backend_ai_grid)
    for i in range(8):
        for j in range(8):
            if frontend_ai_grid[i][j] == 2:
                frontend_ai_grid[i][j] = "M"
            elif frontend_ai_grid[i][j] == "D":
                frontend_ai_grid[i][j] = "H"
            else:
                frontend_ai_grid[i][j] = "#"
                    
    print("Enemy Grid\n")
    print('\n'.join(['   '.join([str(cell) for cell in row]) for row in frontend_ai_grid]))
    
    print("\nYour Grid\n")
    print(print('\n'.join(['   '.join([str(cell) for cell in row]) for row in playergrid]))
)
    frontend_ai_grid.clear()
    
    return backend_ai_grid

def main():
    print("What mode would you like?")
    print("1) Player Vs. AI")
    print("2) Player Vs. Player")
    
    choice = input("Enter your selection:")
    
    start_game_loop(choice)
    
def auto_place_ships(grid):
    for i in range(4):
        coll = random.randint(0, len(grid) - 1)
        row = random.randint(0, len(grid) - 1) ## grid is 8x8
        grid[coll][row] = 1 # true = occupied
    return grid

def manual_place_ships(grid):
    for i in range(1, 6):
        print('\n'.join(['   '.join([str(cell) for cell in row]) for row in grid]))
        print(f"\nEnter where would you like to place your ship ({i}/5):")
                
        row, coll = get_input()
        
        grid[row][coll] = "S"

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
    

def initiate_empty_grid():
    grid = []
    for i in range(8):
        grid.append([])
        for j in range(8):
            grid[i].append("#")
            
    return grid
    
main()
