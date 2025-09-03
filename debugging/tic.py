def print_board(board):
    """Pretty-print the 3x3 board."""
    print("   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  " + " | ".join(row))
        if i < 2:
            print("  " + "-" * 9)

def check_winner(board):
    """
    Return 'X' or 'O' if there's a winner, otherwise None.
    """
    lines = []

    # Rows
    lines.extend(board)

    # Columns
    for c in range(3):
        lines.append([board[r][c] for r in range(3)])

    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] != " " and line.count(line[0]) == 3:
            return line[0]
    return None

def board_full(board):
    """Return True if no empty cells remain."""
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    """
    Prompt for a valid (row, col) in 0..2.
    Re-prompts on non-numeric, out-of-range, or malformed input.
    """
    while True:
        try:
            row_str = input(f"Player {player} — enter row (0, 1, or 2): ").strip()
            col_str = input(f"Player {player} — enter column (0, 1, or 2): ").strip()

            row = int(row_str)
            col = int(col_str)

            if row not in (0, 1, 2) or col not in (0, 1, 2):
                print("Out of range. Please enter 0, 1, or 2.")
                continue

            return row, col
        except ValueError:
            print("Invalid input. Please enter numeric values 0, 1, or 2.")

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Get a valid move
        row, col = get_move(player)

        # Check if the spot is free
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the mark
        board[row][col] = player

        # Check for win
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
