import checkers

def game():
    size = int(input("Enter the square board size (between 4 and 6): "))
    if size < 4 or size > 16:
        print("Invalid board size. Please enter a number between 4 and 6.")
        return
    
    board = build_board(size)
    print("Generated board:")
    print(board)

    empty_count = get_count(board, 'Empty')
    red_count = get_count(board, 'Red')
    black_count = get_count(board, 'Black')

    print(f"Empty cells: {empty_count}")
    print(f"Red checkers: {red_count}")
    print(f"Black checkers: {black_count}")

if __name__ == "__main__":
    game()
