import curses
from utils.ai import BOT_iq0, BOT_iq100
from utils.file_opener import czytanie_wyniki, zapisz_wynik
from utils.menu import menu
import config.config as config
from utils.player import dodaj_wynik, get_player_name, najwyzszywynik
import utils.sound as sound
from utils.winner_checker import Remis, Wygrana

def Game(stdscr):
    
    def initialize_board():
        return {i: " " for i in range(1, 10)}
    
    def start_music():
        if config.difficulty_level == 0:
            sound.play_music('Sound/Battlemusic0.wav', 0.3)
        elif config.difficulty_level == 1:
            sound.play_music('Sound/Battlemusic1.mp3', 0.3)
            
    def display_board():
        stdscr.clear()
        stdscr.addstr(0, 0, "Plansza Gry:")
        for i in range(5):
            for j in range(5):
                if i in [1, 3] and j in [1, 3]:
                    stdscr.addstr(i+1, j, "+")
                elif i in [1, 3]:
                    stdscr.addstr(i+1, j, "-")
                elif j in [1, 3]:
                    stdscr.addstr(i+1, j, "|")
                
                if i % 2 == 0 and j % 2 == 0:  # Only for positions 0, 2, 4 in x and y
                    pos = (i // 2) * 3 + (j // 2) + 1
                    stdscr.addstr(i+1, j, game_board[pos])
                    
                
        stdscr.refresh()
        
    def Wybor(): #funcion that let player choice
        while True:
            try: #only place where player can destroy somthing(I hope so), so Try on the face!
                stdscr.addstr("\ngdzie chcesz postawić 'x' ?: \n")
                
                key = int(chr(stdscr.getch()))

                if game_board[key] == " ":
                    game_board[key] = "X"
                    display_board()
                    return game_board
                elif game_board[key] != " ":
                    stdscr.addstr("Podaj wolne miejsce: ")
                    continue
                
            except:
                stdscr.addstr("Gra przyjmuje tylko '1-9' w liczbach")
                
    def close():
        if najwyzszywynik():
            stdscr.addstr(10, 0, "Twój wynik jest w Top 10!")
            if config.name == None:
                stdscr.addstr(11, 0, "Podaj swoją nazwę: ")
                stdscr.refresh()
                config.name = get_player_name(stdscr)
            dodaj_wynik()
            zapisz_wynik()
        else:
            stdscr.addstr(10, 0, f"Wygrałeś: {config.new_score} razy")
            stdscr.refresh()
        config.new_score = 0
        config.name = None
        sound.stop_music()
    
    curses.curs_set(0)  # Disable cursor
    game_board = initialize_board()
    czytanie_wyniki()


    while True:
        display_board()
        stdscr.addstr(6, 0, f"Poziom: {config.difficulty_level}")

        # Player movement
        game_board = Wybor()
        if Wygrana(game_board, "X"):
            config.new_score += 1
            stdscr.addstr(8, 0, "Wygrałeś! Naciśnij Enter, aby kontynuować...")
            stdscr.refresh()
                
            Decyzja = menu("endgame", )
            if Decyzja == 2:  # Wyjdz
                close()
                return False
            elif Decyzja == 1:  # Kontynuuj
                return True

        if Remis(game_board):
            stdscr.addstr(8, 0, "Remis!")
            stdscr.refresh()

            Decyzja = menu("endgame", stdscr)
            if Decyzja == 2:  # Wyjdz
                close()
                return False
            elif Decyzja == 1:  # Kontynuuj
                return True

        if config.difficulty_level == 1:
            game_board = BOT_iq100(game_board)
        elif config.difficulty_level == 0:
            game_board = BOT_iq0(game_board)

        if Wygrana(game_board, "O"):
            stdscr.addstr(8, 0, "Przegrałeś!")
            stdscr.refresh()
            Decyzja = menu("endgame")
            if Decyzja == 2:  # Wyjdz
                close()
                return False
            elif Decyzja == 1:  # Kontynuuj
                return True
