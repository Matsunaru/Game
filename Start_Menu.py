import os
from Logika import *
import random
import keyboard
import os
from Main_Game import Game
from Opcje import PoziomTrudności
from Logika import czytanie_wyniki
import webbrowser

while True:
    itstart = MenuW("Start","Poziom Trudności","Wyniki","Wyjdz")
# Main Menu with opcion and start game
    if itstart == "Start":
        Game()
    elif itstart == "Poziom Trudności":
        PoziomTrudności()
    elif itstart == "Wyniki":
        while True:
            file_path = "scores.txt"
            scores = czytanie_wyniki(file_path)
            itWynik = MenuW(*scores,"Wyjdz")
            if itWynik == scores[0]:
                webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')#just easter egg
            elif itWynik == "Wyjdz":
                break
            else:
                continue
    elif itstart == "Wyjdz":
        break