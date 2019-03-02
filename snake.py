import pygame

class Snake:
    def __init__(self):
        self.head = [45,45]
        self.body = [[45, 45], [34, 45], [23, 45]] #пробел в один пиксель между квадратами

    def moove(self, control):
        """Движение змеи в зависимости от направления"""
        if control.flag_direction == "RIGHT":
            self.head[0] += 11
        elif control.flag_direction == "LEFT":
            self.head[0] -= 11
        elif control.flag_direction == "UP":
            self.head[1] -= 11
        elif control.flag_direction == "DOWN":
            self.head[1] += 11

    def animation(self):
        """Прибавляем в начало писка тела голову, а хвост удаляем"""
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_snake(self, screen):
        """Отрисовка змеи на экране"""
        for segment in self.body:
            pygame.draw.rect(screen, pygame.Color("Green"), pygame.Rect(segment[0], segment[1], 10, 10))