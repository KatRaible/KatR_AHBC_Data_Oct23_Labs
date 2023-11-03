import numpy as np

def build_board(size):
    choices = ['Empty', 'Red', 'Black']
    board = np.random.choice(choices, size=(size, size))
    return board

def get_count(board, item):
    return np.count_nonzero(board == item)

if __name__ == "__main__":
    print("not the main file")