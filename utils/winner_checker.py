def Wygrana(board,winner):#this funcion cheking if somone win
    if board[1] == board[2] == board[3] and board[2] == winner:
        return True
    elif board[4] == board[5] == board[6] and board[5] == winner:
        return True
    elif board[7] == board[8] == board[9] and board[8] == winner:
        return True
    elif board[1] == board[4] == board[7] and board[4] == winner:
        return True
    elif board[2] == board[5] == board[8] and board[5] == winner:
        return True
    elif board[3] == board[6] == board[9] and board[6] == winner:
        return True
    elif board[1] == board[5] == board[9] and board[5] == winner:
        return True
    elif board[3] == board[5] == board[7] and board[5] == winner:
        return True
    return False

def Remis(board):# checking if this is tie
    if any(board[i] == " "for i in range(1, 10)):
        return False
    return True