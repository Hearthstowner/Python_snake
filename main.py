import sys

import pygame

from snake import Snake
from control import Control
from settings import SIZE, var_speed

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake")
control = Control()
snake = Snake()

while control.flag_game:
    control.control()
    screen.fill(pygame.Color("Black"))
    snake.draw_snake(screen)
    if var_speed % 1000 == 0 and control.flag_pause:
        snake.moove(control)
        snake.animation()
    var_speed += 50 
    pygame.display.flip()
