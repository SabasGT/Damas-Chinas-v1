# Juego de Checkers
import pygame
from checkers.constants import * # Podemos hacer esto porque añadimos el archivo __init__.py a la carpeta, haciendo que Python reconozca todo como un paquete
from checkers.board import Board

# Constantes del Render Engine
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Tamaño de la pantalla
pygame.display.set_caption("Checkers") # Nombre de la ventana del juego

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()

main()
