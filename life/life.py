'''
    +---------+
    |  LIFE   |
    +---------+

'''

import pygame, time, random

# константы
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 5
HEIGHT = 5
MARGIN = 1




# функции
def draw(grid):
    for row in range(len(grid)-1):
        for col in range(len(grid[row])-1):
            if grid[row][col] == 0:
                color = WHITE
            if grid[row][col] == 1:
                color = GREEN
            if grid[row][col] == 2:
                color = BLUE
            if grid[row][col] == 3:
                color = RED
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * col + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])


def process(grid):
    grid_ = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(grid)-1):
        for j in range(len(grid[i])-1):
            currNbr = [grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1], grid[i][j-1], grid[i][j+1], grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]]
            if grid[i][j] == 0 and currNbr.count(1) == 3:
                grid_[i][j] = 1
            elif grid[i][j] == 1 and 2 <= currNbr.count(1) < 4:
                grid_[i][j] = 1
            else:
                grid_[i][j] = 0
    return grid_
            
# матрица

_row = 100
_col = 200

grid = [[0] * _col for _ in range(_row)]

for _ in range(4000):
    grid[random.randint(0, _row-1)][random.randint(0, _col-1)] = 1



# инициализация библиотеки pygame
pygame.init()

# размер экрана
size = ((WIDTH+MARGIN)*_col, (HEIGHT+MARGIN)*_row)
screen = pygame.display.set_mode(size)

# название программы
pygame.display.set_caption('Life 2')

# флаг цикла
flag = True

# ?
clock = pygame.time.Clock()

# main loop
while flag:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    # ---логика программы---
    grid = process(grid)

    # ---отрисовка сцены---
    screen.fill(BLACK)
    draw(grid)
    
    # ---обновление кадров
    pygame.display.flip()
    # time.sleep(1)
    # ?
    clock.tick(60)
pygame.quit()