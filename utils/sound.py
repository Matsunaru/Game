import threading
import time
import pygame


def play_sound_effect(file_path, volume):
    pygame.mixer.init()
    sound_effect = pygame.mixer.Sound(file_path)
    sound_effect.set_volume(volume)
    sound_effect.play()
    
def play_music(file_path, volume):
    threading.Thread(target=music_thread_function, args=(file_path, volume)).start()

def music_thread_function(file_path, volume):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    
    
def stop_music():
    pygame.mixer.music.stop()