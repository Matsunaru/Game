import os
import config.config as config

scores = "scores.txt"
settings = "settings"

def file_exists():
    if not os.path.exists(scores):
        with open(scores, 'w') as file:
            file.write("Rick,1000\nTOP2, 0\nTop3, 0\nTop4, 0\nTOP5, 0\nTOP6, 0\nTOP7, 0\nTOP8, 0\nTop9, 0\nTop10, 0\n")
    if not os.path.exists(settings):
        with open(settings, 'w') as file:
            file.write("0")
            config.difficulty_level = 0
    else:
        with open(settings, 'r') as file:
            config.difficulty_level = int(file.read())

def czytanie_wyniki():#reading scoreboard from file, and puting it in tuple
    config.scores = []
    with open(scores, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')
            config.scores.append((name, int(score)))

def zapisz_wynik():#save scores tuple in to the file txt
    with open(scores, 'w') as file:
        for name, score in config.scores:
            file.write(f"{name},{score}\n")

def zapisz_opcje():
    with open(settings, 'w') as file:
        file.write(str(config.difficulty_level))