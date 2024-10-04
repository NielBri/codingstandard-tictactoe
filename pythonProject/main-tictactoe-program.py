# Program that can let you play tic tac toe

# Make a grid or place to play
grid = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

player = "X"
winner = None
game_running = True

# Visual representation of the play space or grid
def print_grid(grid):
    print("  " + grid[0] + " | " + grid[1] + " | " + grid[2])
    print("-------------")
    print("  " + grid[3] + " | " + grid[4] + " | " + grid[5])
    print("-------------")
    print("  " + grid[6] + " | " + grid[7] + " | " + grid[8])

# Detect player input
def player_input(grid):
    while True:
        if player == "X":
            inp = int(input("Player (X) please choose a number between 1-9 as represented in the grid: "))
        else:
            inp = int(input("Player (O) please choose a number between 1-9 as represented in the grid: "))
        if inp >= 1 and inp <= 9 and grid[inp-1] == "-":
            grid[inp-1] = player
            break
        else:
            if player == "X":
                print("Failure. Try agin Player (X)")
            else:
                print("Failure. Try agin Player (O)")
            print_grid(grid)

# Check whether there is a tie or winner in a horizontal line
def check_place_horizontal(grid):
    global winner
    if grid[0] == grid[1] == grid[2] and grid[0] != "-":
        winner = grid[0]
        return True
    elif grid[3] == grid[4] == grid[5] and grid[3] != "-":
        winner = grid[3]
        return True
    elif grid[6] == grid[7] == grid[8] and grid[6] != "-":
        winner = grid[6]
        return True

# Check whether there is a tie or winner in a vertical line
def check_place_vertical(grid):
    global winner
    if grid[0] == grid[3] == grid[6] and grid[0] != "-":
        winner = grid[0]
        return True
    elif grid[1] == grid[4] == grid[7] and grid[1] != "-":
        winner = grid[1]
        return True
    elif grid[2] == grid[5] == grid[8] and grid[2] != "-":
        winner = grid[2]
        return True

# Check whether there is a tie or winner in a diagonal line
def check_place_diagonal(grid):
    global winner
    if grid[0] == grid[4] == grid[8] and grid[0] != "-":
        winner = grid[0]
        return True
    elif grid[2] == grid[4] == grid[6] and grid[2] != "-":
        winner = grid[2]
        return True

# Switch players X and O
def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"