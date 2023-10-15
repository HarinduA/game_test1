def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True

    if [board[i][i] for i in range(3)].count(player) == 3 or \
       [board[i][2-i] for i in range(3)].count(player) == 3:
        return True

    return False

def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. That spot is already taken.contact harindu")

if __name__ == "__main__":
    play_game()
