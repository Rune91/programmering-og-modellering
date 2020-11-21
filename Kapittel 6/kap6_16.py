import pygame
from sys import exit

pygame.init()
overflate = pygame.display.set_mode( (490, 276) )
pygame.display.set_caption("Opggave 6.16")

bilde1 = pygame.image.load("bilder/erna1.png")
bilde2 = pygame.image.load("bilder/erna2.png")
bilde3 = pygame.image.load("bilder/erna3.png")
bilde4 = pygame.image.load("bilder/erna4.png")

overflate.blit(bilde3, (0, 0))
overflate.blit(bilde1, (20, 30))
overflate.blit(bilde2, (350, 80))
overflate.blit(bilde4, (280, 150))
pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()