import random
import copy

def check_game_status(grid):
    found_occupied = False
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
    
    print('\n'.join(['   '.join([str(cell) for cell in row]) for row in player_grid]))

    
    if game_mode == "1":
        ##generate AI grid
        backend_ai_grid = auto_place_ships(initiate_empty_grid())
    while True: 
        backend_ai_grid = player_turn(backend_ai_grid)
        
        if check_game_status(backend_ai_grid) == "Over":
            print("Game Over!")
            break

def ai_turn(backend_ai_grid):
    pass

def player_turn(backend_ai_grid):
    row = int(input("Enter collumn you would like to attack (Horizontal):"))
    coll = int(input("Enter row you would like to attack (Vertical):"))
        
    if 0 <= coll < 8 and 0 <= row < 8:
        hit = check_hit(backend_ai_grid, row - 1, coll - 1)
        print(hit)
        if hit == "Hit!":
            backend_ai_grid[coll - 1][row - 1] = "D"
        else:
            backend_ai_grid[coll - 1][row - 1] = 2

    frontend_ai_grid = copy.deepcopy(backend_ai_grid)
    for i in range(8):
        for j in range(8):
            if frontend_ai_grid[i][j] == 2:
                frontend_ai_grid[i][j] = "M"
            elif frontend_ai_grid[i][j] == "D":
                frontend_ai_grid[i][j] = "H"
            else:
                frontend_ai_grid[i][j] = "#"
                    
    print('\n'.join(['   '.join([str(cell) for cell in row]) for row in frontend_ai_grid]))
        
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
    print('\n'.join(['   '.join([str(cell) for cell in row]) for row in grid]))
    for i in range(1, 6):
        print(f"\nEnter where would you like to place your ship ({i}/5):")
        coll = int(input("Enter Collumn (Horizontal):"))
        row = int(input("Enter Row (Vertical):"))
        
        if 0 <= coll < 8 and 0 <= row < 8:
            grid[coll][row] = "S"
            
    return grid


def initiate_empty_grid():
    grid = []
    for i in range(8):
        grid.append([])
        for j in range(8):
            grid[i].append(0)
            
    return grid
    
main()
