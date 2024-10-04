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