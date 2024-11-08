import random

def create_board(size=6):
    return[['0'] * size for _ in range(size)]

    def print_board(board):
        print("  " + " ".join(str(i) for i in range(len)(board)))
        
