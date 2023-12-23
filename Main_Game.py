import os
from Logika import *
def Game():
    punkty = 0
    os.system('cls')
    game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}



    while True:
        Plansza(game_board)
        game_board = Wybor(game_board)
        if Wygrana(game_board,"X"):
            os.system('cls')
            Plansza(game_board)
            punkty += 1
            input("Wygrałeś naciśnij Enter, aby kontynuować...")
            Decyzja = MenuW("Kontynuuj","Wyjdz")
            if Decyzja == "Wyjdz":
                print(punkty)
                return
            elif Decyzja == "Kontynuuj":
                game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}
                os.system('cls')
                continue
        if Remis(game_board):
            os.system('cls')
            Plansza(game_board)
            input("Remis naciśnij Enter, aby kontynuować...")
            Decyzja = MenuW("Kontynuuj","Wyjdz")
            if Decyzja == "Wyjdz":
                print(punkty)
                return
            elif Decyzja == "Kontynuuj":
                game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}
                os.system('cls')
                continue

        game_board = BOT_iq0(game_board)
        if Wygrana(game_board,"O"):
            os.system('cls')
            Plansza(game_board)
            input("Pzegrałeś naciśnij Enter, aby kontynuować...")
            Decyzja = MenuW("Kontynuuj","Wyjdz")
            if Decyzja == "Wyjdz":
                print(punkty)
                return
            elif Decyzja == "Kontynuuj":
                game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}
                os.system('cls')
                continue
        os.system('cls')