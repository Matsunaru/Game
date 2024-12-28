import curses
import webbrowser
from src.Main_Game import Game
from utils.opcje import PoziomTrudności
from utils.menu import menu
from utils.file_opener import file_exists, czytanie_wyniki

# Funkcja głównego menu
def main():
    while True:
        itstart = menu("main")

        # Główne menu z opcjami i uruchamianiem gry
        if itstart == 1:
            while curses.wrapper(Game):
                pass
        elif itstart == 2:
            PoziomTrudności()
        elif itstart == 3:
            while True:
                try:
                    czytanie_wyniki()
                except Exception as e:
                    print(f"Błąd podczas odczytu wyników: {e}")
                    break

                itWynik = menu("leaderboard")

                if itWynik == 1:
                    # Easter egg
                    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')
                elif itWynik == None:
                    break
        elif itstart == 4:
            break

if __name__ == "__main__":
    try:
        file_exists()# Sprawdzenie pliku scores.txt
        main()
    except Exception as e:
        print(f"error:{e}")