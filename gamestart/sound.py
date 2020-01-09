import pygame
import os

def song(song_name):
    if song_name.find('.') == -1:
        module_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(module_path, 'assets', 'sounds', song_name+'.wav')
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(0)