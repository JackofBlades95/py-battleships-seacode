import random

def print_grid(grid):
    """
    Prints the grid.
    """
    for row in grid:
        print(" ".join(row))

        
        def create_grid(size):
            """
            Creates the empty the grid.
            """
            grid = []
            for _ in range(size):
                grid.append(["0"] * size)
                return grid

                
                def place_computer_ship(size):
                    """
                    Place's the computers ship randomly on the grid.
                    """
                    ship_row = random.randint(0, size - 1)
                    ship_col = random.randint(0, size  -1)
                    return (ship_row, ship_col)

                    
                    def get_user_guess():
                        """
                        Get the user's guess and validates it.
                        """
                        while True:
                            try:
                                guess = input("Enter your guess(row,col): ")
                                row, col = map(int, guess.split(","))
                                return (row, col)
                            except ValueError:
                                print("Invalid input. Please enter row and column as two numbers seperated by a comma.")
                            except IndexError:
                                        print("Guess is off the grid. Please try again.")

                                        
                                        def main():
                                            """
                                            Runs all program functions.
                                            """
                                            print("Welcome to Battleships Seacode!")

                                            grid_size = int(input("Enter the grid size (e.g., 5 for a 5x5 grid): "))

                                            grid = create_grid(grid_size)
                                            ship_row, ship_col = place_computer_ship(grid_size)

                                            attempts = 0
                                            max_attempts = 10
                                            
                                            while attempts < max_attempts:
                                                print("\nCurrent Grid:")
                                                print_grid(grid)

                                                user_row, user_col = get_user_guess()

                                                if user_row < 0 or user_row >= grid_size or user_col < 0 or user_col >= grid_size:
                                                    print("Your guess is off the grid. Please try again.")
                                                    continue

                                                attempts += 1

                                                if (user_row == ship_row) and (user_col == ship_col):
                                                    print(f"Good Hit! You hit the enemy ship at ({user_row}, {user_col})!")
                                                    print(f"You sank the ship in {attempts} attempts!")
                                                    break
                                                else:
                                                    grid[user_row][user_col] = "X"
                                                    print("You missed! Try again!")

                                                    if attempts == max_attempts:
                                                        print("\nYou've run out of attempts. The ship was at:")
                                                        print(f"({ship_row}, {ship_col})")
                                                        print("Game over.")

                                                        main()
                                                        