import pygame
from sys import exit

pygame.init()
overflate = pygame.display.set_mode( (300, 300) )
pygame.display.set_caption("Oppgave 6.17")

GREEN = (0, 255, 0)
RED = (255, 0, 0)

overflate.fill(GREEN)
pygame.display.update()

x = 100
y = 100

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            x -= 5
        if pressed_keys[pygame.K_RIGHT]:
            x += 5
        if pressed_keys[pygame.K_UP]:
            y -= 5
        if pressed_keys[pygame.K_DOWN]:
            y += 5
    
    overflate.fill(GREEN)
    pygame.draw.rect(overflate, RED, (x, y, 20, 20), 0)
    pygame.display.update()