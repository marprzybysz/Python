# Główny sterownik (Gamestate oraz Sterowanie figurami)

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512 #400 to inna opcja
DIMENSION = 8 # podanie proporcji szachownicy 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # blokada dla pozniejszych animacji
IMAGES = {}

# Globalna przekierowanie dla plików img
