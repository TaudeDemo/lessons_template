import pygame
import random


class Stars:
    name = 'Stars'

    def __init__(self, count):
        self.count = count
        self.pos_list = []

    def draw(self, screen: pygame.Surface):
        if self.count <= 0:
            screen.set_at(self.pos_list[0], 'black')
            self.pos_list.pop(0)

        width, height = screen.get_size()
        rand_x = random.randint(0, width - 1)
        rand_y = random.randint(0, height - 1)
        self.pos_list.append((rand_x, rand_y))
        screen.set_at((rand_x, rand_y), 'white')
        self.count -= 1
