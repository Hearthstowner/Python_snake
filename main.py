import sys
import pygame

from settings import SIZE, head, var_speed

pygame.init()
screen = pygame.display.set_mode(SIZE)
flag_game = True
pygame.display.set_caption("Snake")

while flag_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_game = False
    screen.fill(pygame.Color("Black"))
    pygame.draw.rect(screen,pygame.Color("Green"), pygame.Rect(head[0], head[1], 10, 10))
    if var_speed % 1000 == 0:
        head[0] += 25
    var_speed += 1 
    pygame.display.flip()

