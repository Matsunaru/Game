from utils.file_opener import zapisz_opcje
from utils.menu import menu
import config.config as config

def PoziomTrudności():
    meniu = menu("difficulty")

    if meniu == 1:
        config.difficulty_level = 0
    elif meniu == 2:
        config.difficulty_level = 1
        
    zapisz_opcje()
    
    return
