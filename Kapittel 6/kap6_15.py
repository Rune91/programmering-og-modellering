import pygame
from sys import exit

pygame.init()
overflate = pygame.display.set_mode( (300, 300) )
pygame.display.set_caption("Mitt første vindu")

GREEN = (0, 255, 0)
bilde = pygame.image.load("pingvin.png")

overflate.fill(GREEN)
overflate.blit(bilde, (75, 75))
pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()