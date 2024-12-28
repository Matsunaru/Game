import config.config as config

def najwyzszywynik():#checking if in scores there are place for new player record
    return len(config.scores) < 10 or config.new_score > min(config.scores, key=lambda x: x[1])[1]

def dodaj_wynik():#adding new scores to the Scores tuple
    config.scores.append((config.name, config.new_score))
    config.scores.sort(key=lambda x: x[1],reverse=True)
    return config.scores[:10]

def get_player_name(stdscr):
        name = ""
        while True:
            key = stdscr.getch()
            if key in [10, 13]:  # Enter key
                break
            elif key in [8, 127]:
                name = name[:-1]
            elif 32 <= key <= 126:  # Printable ASCII characters
                name += chr(key)

            stdscr.addstr(12, 0, " " * 20)  # Clear the line
            stdscr.addstr(12, 0, name)
            stdscr.refresh()
        return name