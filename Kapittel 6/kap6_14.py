import pygame
from sys import exit

pygame.init()
overflate = pygame.display.set_mode( (300, 200) )
pygame.display.set_caption("Oppgave 6.14")

GREEN = (0, 255, 0)

overflate.fill(GREEN)
pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit