import pygame
from sys import exit
from pylab import uniform
from math import pi, atan2, sin, cos, sqrt

class Kant:
    def __init__(self, x, y, vinkel, lengde):
        self.x = x
        self.y = y
        self.vinkel = vinkel
        self.p1 = (x+cos(vinkel)*lengde/2, y+sin(vinkel)*lengde/2)
        self.p2 = (x-cos(vinkel)*lengde/2, y-sin(vinkel)*lengde/2)
    def kollisjon(self, x, y):
        r = pygame.Rect(x-5, y-5, 10, 10)
        return len( r.clipline(self.p1, self.p2) ) > 0

def ny_fart(dx, dy, vinkel):
    v_abs = sqrt(dx**2+dy**2)
    v_in = atan2(dy, dx)
    v_ut = 2*pi - (v_in-2*vinkel)
    return (cos(v_ut)*v_abs, sin(v_ut)*v_abs)

pygame.init()
overflate = pygame.display.set_mode( (300, 300) )
pygame.display.set_caption("Oppgave 6.17")

font = pygame.font.Font(None, 20)
DARK_GRAY = (25, 50, 50)
LIGHT_GRAY = (200, 200, 200)

overflate.fill(DARK_GRAY)
pygame.display.update()

kanter = [ Kant(150, 20, 0, 260), Kant(150, 280, 0, 260),
           Kant(20, 150, pi/2, 260), Kant(280, 150, pi/2, 260)]
x = 120
y = 100
dx = 2
dy = 1

klokke = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            (mus_x, mus_y) = pygame.mouse.get_pos()
            kant = Kant(mus_x, mus_y, uniform(2*pi), 100)
            kanter.append(kant)
    x += dx
    y += dy
    
    overflate.fill(DARK_GRAY)
    tekst = font.render("Trykk med musa", False, LIGHT_GRAY)
    overflate.blit(tekst, (95, 150))
    pygame.draw.circle(overflate, LIGHT_GRAY, (x, y), 5)
    
    for kant in kanter:
        if kant.kollisjon(x, y):
            ny = ny_fart(dx, dy, kant.vinkel)
            dx = ny[0]
            dy = ny[1]
        pygame.draw.aaline(overflate, LIGHT_GRAY, kant.p1, kant.p2)
    
    pygame.display.update()
    klokke.tick(60)