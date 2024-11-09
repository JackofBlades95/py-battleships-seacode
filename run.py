import random

def create_board(size):
    return[['0' for _ in range (size)] for _ in range(size)]

    def print_board(board):
        print("  " + " ".join(str(i) for i in range(len)(board)))
        for i, row in enumerate(board):
            print(f"{i} " + " ".join(row))
    

