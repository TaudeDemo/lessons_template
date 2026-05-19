import pygame
import math


from lessons.color import hsv_to_srgb


class Lines:
    name = 'Lines'

    def __init__(self, screen: pygame.Surface):
        width, height = screen.get_size()
        self.start_point = (width // 2, height // 2)
        self.x = width - 1
        self.y = height - 1
        self.state = 'right'

    def draw(self, screen: pygame.Surface):
        x = self.x
        y = self.y
        state = self.state
        step = 4
        width, height = screen.get_size()
        if state == '':
            return
        hue = math.degrees(math.atan2(y - self.start_point[1], x - self.start_point[0]))
        color = hsv_to_srgb(hue, 1, 1)
        pygame.draw.line(screen, color, self.start_point, (x, y))
        if state == 'right':
            y -= step
            if y < 0:
                state = 'top'
                x = width - 1 + y
                y = 0
        elif state == 'top':
            x -= step
            if x < 0:
                state = 'left'
                y = -x
                x = 0
        elif state == 'left':
            y += step
            if y >= height:
                state = 'bottom'
                x = y - height + 1
                y = height - 1
        elif state == 'bottom':
            x += step
            if x >= width:
                state = ''
        self.state = state
        self.x = x
        self.y = y
