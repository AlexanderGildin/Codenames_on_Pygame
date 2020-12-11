import pygame
import random
import time


# def draw():
#     screen.fill((0, 0, 0))
#     font = pygame.font.Font(None, 50)
#     text = font.render("Игра!", 1, (100, 255, 100))
#     text_x = width // 2 - text.get_width() // 2
#     text_y = height // 2 - text.get_height() // 2
#     text_w = text.get_width()
#     text_h = text.get_height()
#     screen.blit(text, (text_x, text_y))
#     pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)

class t_board:
    def __init__(self, width, height,window_name):
        self.width = width
        self.height = height
        size = (self.width, self.height)
        self.screen = pygame.display.set_mode(size)
        self.screen.fill((200, 200, 200))
        pygame.display.set_caption(window_name)
        self.reset()

    def reset(self):
        self.matrix = [[(0, "слово")] * 5 for _ in range(5)]
        pygame.draw.rect(self.screen, (255, 255, 255), (5, 5, self.width - 10, self.height - 10), 2)
        self.ceil_h = (self.height - 10) // 5
        self.ceil_w = (self.width - 10) // 5
        y, x = 5 + self.ceil_h, 5 + self.ceil_w
        for _ in range(4):
            pygame.draw.line(self.screen, (255, 255, 255), (5, y), (self.width - 5, y), 2)
            pygame.draw.line(self.screen, (255, 255, 255), (x, 5), (x, self.height - 5), 2)
            y += self.ceil_h
            x += self.ceil_w
        pygame.display.flip()


if __name__ == '__main__':
    try:
        f = open('words.txt', 'rt', encoding="utf-8")
    except Exception:
        print('В каталоге программы не найден файл words.txt с набором слов для игры')
        exit(0)
    temp_wds = f.readlines()
    words = set()
    for i in temp_wds:
        words.add(i.rstrip())
    words = list(words)
    pygame.init()
    width, height = 1200, 900
    game_board = t_board(width, height,"codenames on pygame")
    # control_board = t_board(width//2, height//2, "codenames on pygame: панель управления")
    running = True
    time = pygame.time.Clock()
    fps = 20
    while running:
        for event in pygame.event.get():
            print(event)
            if event.type == 1025:
                circle_center_x = event.pos[0]
                circle_center_y = event.pos[1]
                radius = 1
            if event.type == pygame.QUIT:
                running = False
        time.tick(fps)
    pygame.quit()