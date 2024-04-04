import random
import copy
import os
import time
from rich.console import Console
from rich.table import Table

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
    markings = {'sea':'#', 'ship':'█'}  # Use the Full Block character for ships
    
    grid[coords[1]][coords[0]] = markings[marking]

    return grid

def format_table(grid):
    formatted_rows = []

    for row in grid:
        
        formatted_row = '   '.join([str(cell) for cell in row])
        formatted_rows.append(formatted_row)

   
    new_formatted_rows = []
    for row in grid:
        new_row = ""
        i = 0
        while i < len(row):
            new_row += row[i]
            
            if i < len(row) -1 and row[i] == '█' and row[i + 1] == '█':
                new_row += '███████████'  
                i += 1  
            elif row[i] == '█':
                new_row += '\b\b███    '
            else:
                new_row += '     '
            i += 1
        new_formatted_rows.append(new_row)
    
    formatted_grid = '\n'.join(new_formatted_rows)

    return formatted_grid

def place_ships_manually(grid):
    ships = {'aircraft carrier':5, 'destroyer':3, 'submarine':2, 'patrol boat':1}
    
    print("Admiral! Position your ships for battle!\n")
    print("(Hint: Use the arrow keys to move ship and R to rotate.\nPress enter to confirm ship placement!)")
    for i in range(1, len(ships)):
        print("Admiral, here is a map of the sea!\n")
        print(f"Position your aircraft carrier! ({i}/5)")
        
        for ship, length in ships.items():
            rotation = 0
            ship_tiles = []

            for i in range(2, length + 2):
                grid = mark_tile((i,4), grid, 'ship')
                ship_tiles.append((i, 4))
            
            formatted_grid = format_table(grid)
            print(formatted_grid)
            formatted_grid = None
            
            while True:
                move = input()

                if move == "r":
                    if rotation == 0:
                        rotation = 1
                        midship = ship_tiles[int(length / 2)]

                        for tile in ship_tiles:
                            grid = mark_tile(tile, grid, 'sea')

                        new_ship_tiles = []
                        for i in range(length):
                            new_tile = (midship[1], midship[0] + (i - 1))
                            new_ship_tiles.append(new_tile)
                            
                        for tile in new_ship_tiles:
                            grid = mark_tile(tile, grid, 'ship')

                        print(format_table(grid))
                    else:
                        pass



empty_grid = initiate_empty_grid()
place_ships_manually(empty_grid)

