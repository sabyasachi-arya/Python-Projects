import tkinter as tk
import math


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth+1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth+1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score


def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def button_click(row, col):
    if board[row][col] == " " and not game_over[0]:
        board[row][col] = "X"
        buttons[row][col].config(text="X")
        if check_winner(board, "X"):
            label.config(text="🎉 You win!")
            game_over[0] = True
            return
        if is_full(board):
            label.config(text="It's a draw!")
            game_over[0] = True
            return

        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        buttons[ai_row][ai_col].config(text="O")
        if check_winner(board, "O"):
            label.config(text="🤖 AI wins!")
            game_over[0] = True
        elif is_full(board):
            label.config(text="It's a draw!")
            game_over[0] = True


def restart_game():
    global board, game_over
    board = [[" " for _ in range(3)] for _ in range(3)]
    game_over[0] = False
    label.config(text="Your turn!")
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ")


root = tk.Tk()
root.title("Tic Tac Toe with AI by Saby")

board = [[" " for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
game_over = [False]

label = tk.Label(root, text="Your turn!", font=("Arial", 16))
label.pack()

frame = tk.Frame(root)
frame.pack()

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(frame, text=" ", font=("Arial", 20), width=5, height=2,
                                  command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

restart_button = tk.Button(root, text="Restart Game", font=("Arial", 14), command=restart_game)
restart_button.pack(pady=10)

root.mainloop()
