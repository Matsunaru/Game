import os
from Logika import *
import Opcje
def Game():
    punkty = 0
    os.system('cls')
    game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}
    PoziomH = Opcje.poziomt


    while True:
        Plansza(game_board)
        print(PoziomH)
        # Player movment
        game_board = Wybor(game_board)
        if Wygrana(game_board,"X"): #cheking if player win
            os.system('cls')
            Plansza(game_board)
            punkty += 1
            input("Wygrałeś naciśnij Enter, aby kontynuować...")
            Decyzja = MenuW("Kontynuuj","Wyjdz")
            if Decyzja == "Wyjdz": #player choice if he want continue or not
                print(punkty)
                return
            elif Decyzja == "Kontynuuj":
                game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}
                os.system('cls')
                continue
        if Remis(game_board): #Tai
            os.system('cls')
            Plansza(game_board)
            input("Remis naciśnij Enter, aby kontynuować...")
            Decyzja = MenuW("Kontynuuj","Wyjdz")
            if Decyzja == "Wyjdz": #Again player choice
                print(punkty)
                return
            elif Decyzja == "Kontynuuj":
                game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}
                os.system('cls')
                continue
        if PoziomH == 1:
            game_board = BOT_iq100(game_board)
        elif PoziomH == 0:
            game_board = BOT_iq0(game_board)
        if Wygrana(game_board,"O"): #checking if, Bot win
            os.system('cls')
            Plansza(game_board)
            input("Pzegrałeś naciśnij Enter, aby kontynuować...")
            Decyzja = MenuW("Kontynuuj","Wyjdz")
            if Decyzja == "Wyjdz": #again plyer choice to continue or quit
                print(punkty)
                return
            elif Decyzja == "Kontynuuj":
                game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}
                os.system('cls')
                continue
        os.system('cls')