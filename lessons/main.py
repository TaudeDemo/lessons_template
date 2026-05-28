import pygame

from lessons import stars
from lessons.lines import Lines
from lessons.stars import Stars

SIZE = (640, 480)
# SIZE = (320, 240)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE, pygame.SCALED, vsync=True)
    font = pygame.font.SysFont('Arial', 18, bold=False)

    scena = Stars(100)

    pygame.display.set_caption('Pygame - ' + scena.name)
    screen.fill('black')
    clock = pygame.time.Clock()
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        scena.draw(screen)

        # draw_fps_counter(screen, font, clock)
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()


def draw_fps_counter(screen, font, clock):
    fps = str(round(clock.get_fps(), 1))
    fps_t = font.render(fps, 1, pygame.Color('RED'), 'black')
    screen.blit(fps_t, (0, 0))
