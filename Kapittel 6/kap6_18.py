import pygame
from sys import exit

def skriv(tekst, storrelse, x, y, farge):
    font = pygame.font.Font(None, storrelse)
    tekst_flate = font.render(tekst, True, farge)
    tekst_rect = tekst_flate.get_rect()
    tekst_rect.left = x
    tekst_rect.top = y
    overflate.blit(tekst_flate, tekst_rect)

pygame.init()
overflate = pygame.display.set_mode( (300, 100) )
pygame.display.set_caption("Oppgave 6.17")

GREEN = (0, 255, 0)
RED = (255, 0, 0)

overflate.fill(GREEN)
pygame.display.update()

x = 100
y = 100

show_box = False

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            show_box = True
        else:
            show_box = False
    
    overflate.fill(GREEN)
    if show_box:
        skriv("Hei, jeg er en boks!", 40, 20, 30, RED)
    pygame.display.update()