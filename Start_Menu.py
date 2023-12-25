import os
from Logika import *
import random
import keyboard
import os
from Main_Game import Game
from Opcje import PoziomTrudności
while True:
    itstart = MenuW("Start","Opcje","Wyniki","Wyjdz")
# Main Menu with opcion and start game
    if itstart == "Start":
        Game()
    elif itstart == "Opcje":
        PoziomTrudności()
    elif itstart == "Wyniki":
        print("ITSTARTWITHNO")
    elif itstart == "Wyjdz":
        break