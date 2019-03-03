import sys

import pygame

from snake import Snake
from control import Control
from settings import SIZE, var_speed
from gui import Gui
from food import Food

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake")
control = Control()
gui = Gui()
gui.init_field() 
food = Food()
food.get_food_position(gui)
gui.init_field()
snake = Snake()

#игровой цикл
while control.flag_game:
    control.control()
    screen.fill(pygame.Color("Black")) 
    snake.draw_snake(screen)
    food.draw_food(screen)
    gui.draw_level(screen)

    if var_speed % 1000 == 0 and control.flag_pause:
        snake.moove(control)
        snake.eat(food, gui)
        snake.check_end_window()
        snake.animation()
    var_speed += 50 
    pygame.display.flip()
