import pygame
import random
import time


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


def draw2(x ,y):
    global radius
    screen.fill((0, 0, 255))
    pygame.draw.circle(screen, (255, 255, 0), (x, y), radius)
    radius += 1
    if radius > 500:
        radius = -3
    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    width, height = 800, 600
    size = (width, height)
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 255))
    pygame.display.flip()
    pygame.display.set_caption('Цветные линии')
    running = True
    time = pygame.time.Clock()
    fps = 20
    radius = -3
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == 768 and event.scancode == 81:
                fps -= 1
            if event.type == 768 and event.scancode == 82:
                fps += 1
            if event.type == 1025:
                circle_center_x = event.pos[0]
                circle_center_y = event.pos[1]
                radius = 1
            if event.type == pygame.QUIT:
                running = False
        if radius > -3:
            draw2(circle_center_x, circle_center_y)
        time.tick(fps)
    pygame.quit()
