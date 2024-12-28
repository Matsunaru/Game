import random

from utils.winner_checker import Remis, Wygrana


def BOT_iq0(board):#Random number generaitor for computer
    while True:
        ran = random.randint(2, 10)
        
        if board[ran - 1] == " ":
            board[ran - 1] = "O"
            return board
        elif board[ran - 1] != " " and any(board[i] == " " for i in range(1, 10)):
            continue
        else:
            return board
        
def minimax(board,depth, is_maximazing):#Minimax
    if Wygrana(board, "X"):
        return -1
    elif Wygrana(board, "O"):
        return 1
    elif Remis(board):
        return 0
    if is_maximazing: #this cheking for computer moves
        BS = float("-inf")
        for i in range(2,11):
            if board[i - 1] == " ":
                board[i - 1] = "O"
                score = minimax(board,depth + 1,False)
                board[i - 1] = " "
                BS = max(score,BS)
        return BS
    else:
        BS = float("inf") #this cheking for enemy moves
        for i in range(2,11):
            if board[i - 1] == " ":
                board[i - 1] = "X"
                score = minimax(board,depth + 1,True)
                board[i - 1] = " "
                BS = min(score,BS)
        return BS
        
def BOT_iq100(board): #computer but useing minimax algorithm
    BS = float("-inf")
    BM = None
    for _ in range(100):
        ran = random.randint(2, 10)
        
        if board[ran - 1] == " ":
            board[ran - 1] = "O"
            score = minimax(board, 0,False)
            board[ran - 1] = " "
            if score > BS:
                BS = score
                BM = ran
    if BM is not None:
        board[BM - 1] = "O"
    return board

