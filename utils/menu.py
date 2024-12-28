import curses
import config.config as config
from utils.sound import play_sound_effect

def load_menu_choices(menu_type):
    if menu_type == "leaderboard":
        return {i + 1: f"{score}" for i, score in enumerate(config.scores)}
    return config.MENU_CHOICES.get(menu_type, {})

def menu(menu_type, stdscr=None, win=None):
    choices = load_menu_choices(menu_type)
    if not choices:
        print("Nie znaleziono opcji dla tego menu.")
        return None

    keys = list(choices.keys())
    selected_index = config.difficulty_level if menu_type == "difficulty" else 0

    def draw_menu(stdscr):
        nonlocal selected_index
        curses.curs_set(0)  # Disable cursor

        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, f"-- {menu_type.capitalize()} Menu --")

            for i, key in enumerate(keys):
                prefix = "> " if i == selected_index else "  "
                stdscr.addstr(i + 2, 2, f"{prefix}{choices[key]}")

            if (menu_type == "difficulty" or menu_type == "leaderboard"):
                back_prefix = "> " if selected_index == len(keys) else "  "
                stdscr.addstr(len(keys) + 3, 2, f"{back_prefix}Powrót")
                
            if menu_type == 'endgame':
                if win == 1:
                    stdscr.addstr(5, 0, f"-- Wygrales --")
                elif win == 0:
                    stdscr.addstr(5, 0, f"-- Remis --")
                elif win == -1:
                    stdscr.addstr(5, 0, f"-- Przegrales --")

            stdscr.refresh()
            key = stdscr.getch()

            if key in [curses.KEY_DOWN, ord('s')]:
                selected_index = (selected_index + 1) % (len(keys) + (1 if (menu_type == "difficulty" or menu_type == "leaderboard") else 0))
                play_sound_effect('Sound/UpDown.mp3', 1.0)
            elif key in [curses.KEY_UP, ord('w')]:
                selected_index = (selected_index - 1) % (len(keys) + (1 if (menu_type == "difficulty" or menu_type == "leaderboard") else 0))
                play_sound_effect('Sound/UpDown.mp3', 1.0)
            elif key in [10, 13]:  # Enter key
                play_sound_effect('Sound/Enter.mp3', 1.0)
                if (menu_type == "difficulty" or menu_type == "leaderboard") and selected_index == len(keys):
                    return None
                else:
                    return keys[selected_index]

    if stdscr:
        return draw_menu(stdscr)
    else:
        return curses.wrapper(draw_menu)
