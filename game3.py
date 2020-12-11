import pygame
from random import random

SIZE = 800, 800

SCREEN = pygame.display.set_mode(SIZE)


def main():
    try:
        pygame.init()
        doing = True
        new_c = False
        v = 10
        fps = 30
        pick = []
        tick = pygame.time.Clock()
        while doing:
            SCREEN.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    doing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    new_c = True
            if new_c:
                pick.append([event.pos, 30, 30])
                new_c = False
            for i in range(len(pick)):
                pygame.draw.circle(SCREEN, (255, 255, 255), (pick[i][0][0], pick[i][0][1]), 10)
                if pick[i][0][0] - pick[i][1] < 0:
                    pick[i][1] = -30

                elif pick[i][0][0] - pick[i][1] > SIZE[0]:
                    pick[i][1] = 30

                if pick[i][0][1] - pick[i][2] < 0:
                    pick[i][2] = -30

                elif pick[i][0][1] - pick[i][2] > SIZE[1]:
                    pick[i][2] = 30

                pick[i][0] = (pick[i][0][0] - pick[i][1], pick[i][0][1] - pick[i][2])
            tick.tick(fps)
            pygame.display.flip()
    except Exception as e:
        print(e)
    pygame.quit()


if __name__ == '__main__':
    main()
