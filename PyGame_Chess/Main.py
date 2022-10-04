import pygame
from pygame.locals import *


pygame.init()
x = 800
y = 600

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEiSS   = ( 255, 255, 255)

fenster = pygame.display.set_mode((x, y))
pygame.display.set_caption("Pygame-Spiel: Chess | By Mario + Andre")
img = pygame.image.load("gameboard2.png")

fenster.blit(img, (20, 20))
pygame.draw.rect(fenster, ROT, [20, 20, 400, 400], 3)



pygame.display.flip()
status = True

while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
 
pygame.quit()
            
