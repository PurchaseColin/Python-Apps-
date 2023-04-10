import pygame 
from checkers.board import Board 

WIDTH, HEIGHT = 800,800
FPS = 60 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def main(): 
 run = True 
 clock = pygame.time.Clock()
 board = Board()

 while run: 
  for event in pygame.event.get(): 
   if event.type == pygame.QUIT : 
    run = False 
  
  board.draw_squares(WIN)
  pygame.display.update()

 pygame.quit()


main()

