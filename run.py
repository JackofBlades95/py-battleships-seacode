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
