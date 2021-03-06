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
    gui.check_win_or_lose()
    control.control()
    screen.fill(pygame.Color("Black")) 
    if gui.game == "GAME":
        snake.draw_snake(screen)
        food.draw_food(screen)
    elif gui.game == "WIN":
        gui.draw_win(screen)
    elif gui.game == "LOSE":
        gui.draw_lose(screen)
    gui.draw_indicator(screen)
    gui.draw_level(screen)

    if var_speed % 1000 == 0 and control.flag_pause and gui.game == "GAME":
        snake.moove(control)
        snake.check_barrier(gui)
        snake.eat(food, gui)
        snake.check_end_window()
        snake.animation()
    var_speed += 50
    pygame.display.flip()
 