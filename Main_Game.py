import os
from Logika import *
punkty = 0
os.system('cls')
game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}


i = 0
while True:
    game_board = Wybor(game_board)
    if Wygrana(game_board):
        punkty += 1
        Decyzja = MenuW()
        if Decyzja == "Wyjdz":
            print(punkty)
            break
        elif Decyzja == "Kontynuuj":
            game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}
            continue

    game_board = BOT_iq0(game_board)
    os.system('cls')
    
    
    
    print(game_board[1],"|",game_board[2],"|",game_board[3])
    print("__________")
    print(game_board[4],"|",game_board[5],"|",game_board[6])
    print("__________",)
    print(game_board[7],"|",game_board[8],"|",game_board[9])
    
