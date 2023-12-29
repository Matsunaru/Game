import random
import keyboard
import os
import pygame
import threading
import time
punkty = 0


def Wybor(board): #funcion that let player choice
    while True:
        try: #only place where player can destroy somthing(I hope so), so Try on the face!
            player = int(input("gdzie chcesz postawić 'x' ?: \n"))
            if board[player] == " ":
                board[player] = "X"
                return board
            elif board[player] != " ":
                print("Podaj wolne miejsce: ")
                continue
        except:
            print("Gra przyjmuje tylko '1-9' w liczbach")
    

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

#interactive menus *args allow you to place as many arguments as you need
def MenuW(*args):
    choices = [arg for arg in args if arg]
    selected_index = 0

    while True:#loop need bcs player need to move around all time
        os.system('cls')

        for i, choice in enumerate(choices):#this print menu
            if i == selected_index:
                print(f"> {choice}")
            else:
                print(f"  {choice}")

        key_event = keyboard.read_event(suppress=True)#read input from keyboard

        if key_event.event_type == keyboard.KEY_UP: #without it,will read press input and release of the key
            continue

        if key_event.name == 'down': # this move you down
            selected_index = (selected_index + 1) % len(choices)
            play_sound_effect('Sound/UpDown.mp3',1.0)
        elif key_event.name == 'up': #this up
            selected_index = (selected_index - 1) % len(choices)
            play_sound_effect('Sound/UpDown.mp3',1.0)
        elif key_event.name == 'enter': #confirm buttom
            print(f"Wybrano: {choices[selected_index]}")
            play_sound_effect('Sound/Enter.mp3',1.0)
            return choices[selected_index]

def Plansza(game_board): #print Board
    print(game_board[7],"|",game_board[8],"|",game_board[9])
    print("__________")
    print(game_board[4],"|",game_board[5],"|",game_board[6])
    print("__________",)
    print(game_board[1],"|",game_board[2],"|",game_board[3])


def Remis(board):# checking if this is tie
    if any(board[i] == " "for i in range(1, 10)):
        return False
    return True

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
    
def czytanie_wyniki(file_path):#reading scoreboard from file, and puting it in tuple
    scores = []
    with open(file_path, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')
            scores.append((name, int(score)))
    return scores

def najwyzszywynik(scores, new_score):#checking if in scores there are place for new player record
    return len(scores) < 10 or new_score > min(scores, key=lambda x: x[1])[1]

def dodaj_wynik(scores,new_score,new_name):#adding new scores to the Scores tuple
    scores.append((new_name,new_score))
    scores.sort(key=lambda x: x[1],reverse=True)
    return scores[:10]

def zapisz_wynik(file_path,scores):#save scores tuple in to the file txt
    with open(file_path, 'w') as file:
        for name, score in scores:
            file.write(f"{name},{score}\n")

def zapytaj_nazwe():#asking player for the name
    return input("Jesteś w top 10 podaj swoją nazwe:")

def play_sound_effect(file_path, volume):
    pygame.mixer.init()
    sound_effect = pygame.mixer.Sound(file_path)
    sound_effect.set_volume(volume)
    sound_effect.play()

def play_music(file_path,volume):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)


def stop_music():
    pygame.mixer.music.stop()

def music_thread_function(file_path, volume):
    play_music(file_path, volume)
    while pygame.mixer.music.get_busy():
        time.sleep(1)