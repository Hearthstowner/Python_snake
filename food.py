import pygame
import random
from gui import Gui

class Food:
    def __init__(self):
        self.food_position = []

    def get_food_position(self, gui):
        """Выдает значение координат для еды"""
        self.food_position = random.choice(gui.field)

    def draw_food(self, screen):
        """Отрисовывыет еду"""
        pygame.draw.rect(screen, pygame.Color("Red"), pygame.Rect(self.food_position[0], self.food_position[1], 10, 10))
       


