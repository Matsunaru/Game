import os
from Logika import *
import random
import keyboard
import os
from Main_Game import Game
while True:
    itstart = MenuW("Start","Opcje","Wyniki","Wyjdz")
# Main Menu with opcion and start game
    if itstart == "Start":
        Game()
    elif itstart == "Opcje":
        print("ISSTARTWITHWHY")
    elif itstart == "Wyniki":
        print("ITSTARTWITHNO")
    elif itstart == "Wyjdz":
        break