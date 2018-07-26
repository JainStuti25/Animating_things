import pygame
import time
pygame.init()
height = 600
width = 600
screen = pygame.display.set_mode((height,width))

pygame.display.set_caption("My Screeen!!")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)

screen.fill(CYAN)
pygame.display.flip()

r = pygame.Rect((3,3), (100,200))

pygame.draw.rect(screen, LIME, r)
pygame.display.flip()

r = r.move((100,100))
r.centerx = width/2
r.centery = height/2

for _ in range(0,100):
    r.x += 1
    screen.fill(CYAN)
    pygame.draw.rect(screen, LIME, r)
    pygame.display.flip()
    time.sleep(0.1)
c = pygame.draw.circle(screen, RED, (50,50), 30)
pygame.display.flip()
c.colliderect(r)


