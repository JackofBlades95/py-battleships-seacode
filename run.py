import random

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

        
        def create_grid(size):
            grid = []
            for _ in range(size):
                grid.append(["0"] * size)
                return grid

                
                def place_computer_ship(size):
                    ship_row = random.randint(0, size - 1)
                    ship_col = random.randint(0, size  -1)
                    return (ship_row, ship_col)

                    
                    def get_user_guess():
                        while True:
                            try:
                                guess = input("Enter your guess(row,col): ")
                                row, col = map(int, guess.split(","))
                                return (row, col)
                                except ValueError:
                                    print("Invalid input. Please enter row and column as two numbers seperated by a comma.")
                                    except IndexError:
                                        print("Guess is off the grid. Please try again.")
