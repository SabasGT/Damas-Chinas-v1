# Archivo que contiene todas las constantes
import pygame

# Pantalla
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# Colores RGB
RED = (255,0,0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (35, 20))
