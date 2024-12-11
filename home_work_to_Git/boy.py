import random

BOARD_SIZE = 10

def create_board():
    """Creates an empty game board."""
    return [['X'] * BOARD_SIZE for _ in range(BOARD_SIZE)]

def place_ships(board, num_ships):
    """Randomly places ships on the board."""
    ships_placed = 0
    while ships_placed < num_ships:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if board[row][col] == 'X':
            board[row][col] = 'S'
            ships_placed += 1
    return board

def print_board(board):
    """Prints the game board."""
    print("  " + " ".join([str(i) for i in range(BOARD_SIZE)]))
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join(row))

def get_player_move():
    """Gets valid player move coordinates."""
    while True:
        try:
            row = int(input("Enter row (0-9): "))
            col = int(input("Enter column (0-9): "))
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                return row, col
            else:
                print("Invalid coordinates. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def check_win(board):
    """Checks if all ships have been sunk."""
    for row in board:
        if 'S' in row:
            return False
    return True

def play_game():
    """Plays a game of Battleship."""
    player_board = create_board()
    computer_board = place_ships(create_board(), 5)  # 5 ships for the computer

    print("Welcome to Battleship!")
    print("Your board:")
    print_board(player_board)

    while True:
        print("\nYour turn!")
        row, col = get_player_move()

        if computer_board[row][col] == 'S':
            print("Hit!")
            computer_board[row][col] = 'X'
            print_board(computer_board)
            if check_win(computer_board):
                print("Congratulations! You sunk all the ships!")
                break
        else:
            print("Miss!")
            computer_board[row][col] = 'M'
            print_board(computer_board)

if __name__ == "__main__":
    play_game()