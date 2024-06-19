# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        # Print each row of the board
        print(" | ".join(row))
        print("-" * 10)  # Print the separator line

# Function to check for a winner in the board
def check_winner(board):
    # Generate all possible winning lines (rows, columns, diagonals)
    lines = board + [list(col) for col in zip(*board)] + [
        [board[i][i] for i in range(len(board))],
        [board[i][len(board) - 1 - i] for i in range(len(board))]
    ]
    # Check each line to see if all elements are the same and not empty space
    for line in lines:
        if line.count(line[0]) == len(line) and line[0] != " ":
            return line[0]
    return None  # No winner yet

# Function to check if the board is full (no more moves possible)
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to make a move on the board
def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False  # Invalid move

# Function to get all available moves on the board
def available_moves(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == " "]

# Minimax algorithm with Alpha-Beta pruning for optimal move selection
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -1  # Score for maximizing player
    elif winner == "O":
        return 1   # Score for minimizing player
    elif is_full(board):
        return 0  # Draw

    if is_maximizing:
        max_eval = float('-inf')
        for (i, j) in available_moves(board):
            board[i][j] = "O"  # AI's move
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for (i, j) in available_moves(board):
            board[i][j] = "X"  # Human's move
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to determine the best move for the AI player
def best_move(board):
    best_val = float('-inf')
    best_move = None
    for (i, j) in available_moves(board):
        board[i][j] = "O"  # Temporarily make the move
        move_val = minimax(board, 0, False, float('-inf'), float('inf'))
        board[i][j] = " "
        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val
    return best_move

# Main function to play the Tic-Tac-Toe game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    ai = "O"
    current_player = human

    while True:
        print_board(board)
        if current_player == human:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if not make_move(board, row, col, human):
                print("Invalid move. Try again.")
                continue
        else:
            move = best_move(board)
            make_move(board, move[0], move[1], ai)
            print(f"AI placed 'O' in position ({move[0]}, {move[1]})")

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = human if current_player == ai else ai  # Switch player

if __name__ == "__main__":
    play_game()
