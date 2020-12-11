import pygame
import random


def draw():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Игра!", 1, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)


def draw1():
    screen.fill((0, 0, 0))
    x0 = width // 2
    y0 = height // 2
    for i in range(150):
        x = random.randint(10, width - 10)
        y = random.randint(10, height - 10)
        rand_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        pygame.draw.line(screen, rand_color, (x0, y0), (x, y), width=1)
        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    width, height = 800, 600
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Цветные линии')
    while pygame.event.wait().type != pygame.QUIT:
        draw1()
    pygame.quit()
