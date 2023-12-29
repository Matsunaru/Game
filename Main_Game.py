import os
from Logika import *
import Opcje
def Game():
    new_score = 0
    os.system('cls')
    game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}
    PoziomH = Opcje.poziomt
    file_path = "scores.txt"
    scores = czytanie_wyniki(file_path)
    if PoziomH == 0:
        music_thread = threading.Thread(target=music_thread_function, args=('Sound/Battlemusic0.wav', 0.3))
        music_thread.start()
    elif PoziomH == 1:
        music_thread = threading.Thread(target=music_thread_function, args=('Sound/Battlemusic1.mp3', 0.3))
        music_thread.start()
    while True:
        Plansza(game_board)
        print(PoziomH)
        # Player movment
        game_board = Wybor(game_board)
        if Wygrana(game_board,"X"): #cheking if player win
            os.system('cls')
            Plansza(game_board)
            new_score += 1
            input("Wygrałeś naciśnij Enter, aby kontynuować...")
            Decyzja = MenuW("Kontynuuj","Wyjdz")
            if Decyzja == "Wyjdz": #player choice if he want continue or not
                if najwyzszywynik(scores,new_score):#if najwyzszywynik = true is gonna execute this part of code
                    print("Twój wynik jest w Top 10!")
                    new_name = zapytaj_nazwe()
                    scores = dodaj_wynik(scores, new_score, new_name)
                    zapisz_wynik(file_path, scores)
                    stop_music()
                else:
                    print("Wygrałeś: ", new_score,"razy")
                    input("Nacisnij enter,aby przejść do menu głównego")
                    stop_music()
                    
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
                if najwyzszywynik(scores,new_score):
                    print("Twój wynik jest w Top 10!")
                    new_name = zapytaj_nazwe()
                    scores = dodaj_wynik(scores, new_score, new_name)
                    zapisz_wynik(file_path, scores)
                    stop_music()
                else:
                    print("Wygrałeś: ", new_score,"razy")
                    input("Nacisnij enter,aby przejść do menu głównego")
                    stop_music()
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
                if najwyzszywynik(scores,new_score):
                    print("Twój wynik jest w Top 10!")
                    new_name = zapytaj_nazwe()
                    scores = dodaj_wynik(scores, new_score, new_name)
                    zapisz_wynik(file_path, scores)
                    stop_music()
                else:
                    print("Wygrałeś: ", new_score,"razy")
                    input("Nacisnij enter,aby przejść do menu głównego")
                    stop_music()
                return
            elif Decyzja == "Kontynuuj":
                game_board = {1: " ",2: " ", 3: " ",4: " ", 5: " ", 6: " ", 7: " ",8: " ",9: " "}
                os.system('cls')
                continue
        os.system('cls')