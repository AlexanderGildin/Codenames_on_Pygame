import pygame
from random import randint


class Board:
    def __init__(self, row, cols):
        self.rows = row
        self.cols = cols
        self.board = [[[0, 0]] * self.cols for i in range(self.rows)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.type = 0

    def render(self):
        self.x = 10
        self.y = 10
        for i in range(self.rows):
            for j in range(self.cols):
                pygame.draw.rect(SCREEN, (255, 255, 255), [(self.x, self.y), (self.cell_size,
                                                                              self.cell_size)], 1)
                self.x += self.cell_size
            self.y += self.cell_size
            self.x = 10

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def get_cell(self, mouse_posit):
        try:
            number_col = (mouse_posit[1] - self.left) // self.cell_size
            number_row = (mouse_posit[0] - self.top) // self.cell_size
            if number_row > self.cols - 1 or number_col > self.rows - 1 or number_row < 0 or number_col < 0:
                raise Exception
            return number_col, number_row
        except Exception:
            return None


class Minesweeper(Board):
    def __init__(self, rows, cols, mines):
        super().__init__(rows, cols)
        self.board = [[-1] * self.cols for i in range(self.rows)]
        for i in range(mines):
            a, b = randint(0, rows - 1), randint(0, cols - 1)
            self.board[a][b] = 10
        self.render()

    def render(self):
        self.x = 10
        self.y = 10
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 10:
                    pygame.draw.rect(SCREEN, (255, 0, 0), [(self.x, self.y), (self.cell_size,
                                                                              self.cell_size)])
                    pygame.draw.rect(SCREEN, (255, 255, 255), [(self.x, self.y), (self.cell_size,
                                                                                  self.cell_size)], 1)
                else:
                    pygame.draw.rect(SCREEN, (255, 255, 255), [(self.x, self.y), (self.cell_size,
                                                                                  self.cell_size)], 1)
                self.x += self.cell_size
            self.y += self.cell_size
            self.x = 10

    def get_cell_b(self, i, j, board):
        try:
            r = board[i][j]
            return r
        except Exception:
            return None

    def clicked(self, cell):
        try:
            self.x = 10
            self.y = 10
            if self.board[cell[0]][cell[1]] != 10 or self.board[cell[0]][cell[1]] != -1:
                pass
            else:
                self.board[cell[0]][cell[1]] = [0, 0]
                print(self.board[cell[0]][cell[1]])
            for i in range(self.rows):
                for j in range(self.cols):
                    if (i, j) == cell and self.board[i][j] != 10:
                        points = [self.get_cell_b(i, j + 1, self.board),
                                  self.get_cell_b(i + 1, j + 1, self.board), self.get_cell_b(i + 1, j, self.board),
                                  self.get_cell_b(i + 1, j - 1, self.board), self.get_cell_b(i, j - 1, self.board),
                                  self.get_cell_b(i - 1, j - 1, self.board), self.get_cell_b(i - 1, j, self.board),
                                  self.get_cell_b(i - 1, j + 1, self.board)]
                        flag = 0
                        for k in points:
                            if k == 10:
                                flag += 1
                        self.board[i][j] = [0, flag]
                    if self.board[i][j] != 10 and self.board[i][j] != -1:
                        pygame.draw.rect(SCREEN, (255, 255, 255), [(self.x, self.y), (self.cell_size,
                                                                                      self.cell_size)], 1)
                        font = pygame.font.Font(None, 30)
                        print(self.board[i][j])
                        text = font.render(str(self.board[i][j][1]), 0, (0, 255, 0))
                        SCREEN.blit(text, (self.x, self.y))
                    elif self.board[i][j] == 10:
                        pygame.draw.rect(SCREEN, (255, 0, 0), [(self.x, self.y), (self.cell_size,
                                                                                  self.cell_size)])
                        pygame.draw.rect(SCREEN, (255, 255, 255), [(self.x, self.y), (self.cell_size,
                                                                                      self.cell_size)], 1)
                    else:
                        pygame.draw.rect(SCREEN, (255, 255, 255), [(self.x, self.y), (self.cell_size,
                                                                                      self.cell_size)], 1)
                    self.x += self.cell_size
                self.y += self.cell_size
                self.x = 10
        except Exception:
            pass


SIZE = 800, 800
SCREEN = pygame.display.set_mode(SIZE)


def main():
    pygame.init()
    fps = 60
    doing = True
    SCREEN.fill((0, 0, 0))
    pole = Minesweeper(10, 10, 5)
    pygame.display.flip()
    tick = pygame.time.Clock()
    while doing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doing = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pole.clicked(pole.get_cell(event.pos))
        tick.tick(fps)
        pygame.display.flip()


if __name__ == '__main__':
    main()
