import pygame

class Snake:
    def __init__(self):
        self.head = [45,45]

    def moove(self, control):
        """Движение змеи в зависимости от направления"""
        if control.flag_direction == "RIGHT":
            self.head[0] += 25
        elif control.flag_direction == "LEFT":
            self.head[0] -= 25
        elif control.flag_direction == "UP":
            self.head[1] -= 25
        elif control.flag_direction == "DOWN":
            self.head[1] += 25

    def draw_snake(self, screen):
        """Отрисовка змеи на экране"""
        pygame.draw.rect(screen, pygame.Color("Green"), pygame.Rect(self.head[0],self.head[1], 10, 10))