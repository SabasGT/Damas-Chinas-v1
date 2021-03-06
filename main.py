# Juego de Checkers
from pandas.io.sql import SQLAlchemyRequired
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE # Podemos hacer esto porque añadimos el archivo __init__.py a la carpeta, haciendo que Python reconozca todo como un paquete
from checkers.board import Board

# Constantes del Render Engine
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Tamaño de la pantalla
pygame.display.set_caption("Checkers") # Nombre de la ventana del juego


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col


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
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)
        
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()
