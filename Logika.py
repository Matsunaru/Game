import random
import keyboard
import os
punkty = 0

def Wybor(board):
    while True:
        try:
            player = int(input("gdzie chcesz postawić 'x' ?: \n"))
            if board[player] == " ":
                board[player] = "X"
                return board
            elif board[player] != " ":
                print("Podaj wolne miejsce: ")
                continue
        except:
            print("Gra przyjmuje tylko '1-9' w liczbach")
    

def BOT_iq0(board):
    while True:
        ran = random.randint(2, 10)
        
        if board[ran - 1] == " ":
            board[ran - 1] = "O"
            return board
        elif board[ran - 1] != " " and any(board[i] == " " for i in range(1, 10)):
            continue
        else:
            return board
        
def Wygrana(board,winner):
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

def MenuW(*args):
    choices = [arg for arg in args if arg]
    selected_index = 0

    while True:
        os.system('cls')

        for i, choice in enumerate(choices):
            if i == selected_index:
                print(f"> {choice}")
            else:
                print(f"  {choice}")

        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == keyboard.KEY_UP:
            continue

        if key_event.name == 'down':
            selected_index = (selected_index + 1) % len(choices)
        elif key_event.name == 'up':
            selected_index = (selected_index - 1) % len(choices)
        elif key_event.name == 'enter':
            print(f"Wybrano: {choices[selected_index]}")
            return choices[selected_index]
            break

def Plansza(game_board):
    print(game_board[7],"|",game_board[8],"|",game_board[9])
    print("__________")
    print(game_board[4],"|",game_board[5],"|",game_board[6])
    print("__________",)
    print(game_board[1],"|",game_board[2],"|",game_board[3])


def Remis(board):
    if any(board[i] == " "for i in range(1, 10)):
        return False
    return True