import pygame.draw
from pygame.draw import *
import numpy as np

# ФУНКЦИИ
def home(screen, xh, yh, h):
    '''
    Рисует дом. Параметры:
    screen - объект pygame.Surface
    xh, yh - координаты левого верхнего угла дома
    h - масштаб дома (некоторое положительное число)
    '''
    home_color = (150, 75, 0) # Цвет дома
    roof_color = (255, 0, 0) # Цвет крыши
    window_color = (0, 191, 255) # Цвет окна
    
    rect(screen, home_color, (xh, yh, 150 * h, 100 * h), 0)  # Дом
    polygon(screen, roof_color, [(xh + 150 * h / 2, yh - 100 * h / 2), (xh, yh), (xh + 150 * h, yh)], 0)  # Крыша дома
    rect(screen, window_color, (xh + 50 * h, yh + 30 * h, 50 * h, 30 * h), 0)  # Окно


def tree(screen, xt, yt, t):
    '''
    Рисует дерево. Параметры:
    screen - объектк pygame.Surface
    xt, yt - координаты левого верхнего угла ствола дерева
    t - масштаб дерева
    '''
    log_color = (150, 75, 0) # Цвет ствола
    leaves_color = (1, 50, 32) # Цвет листьев
    
    # Ствол
    rect(screen, log_color, (xt, yt, 15 * t, 60 * t), 0) 
    # Листва
    circle(screen, leaves_color, (xt + 15 * t / 2, yt - 30 * t), 30 * t)
    circle(screen, leaves_color, (xt + 15 * t / 2 + 30 * t, yt - 30 * t + 15 * t), 30 * t)
    circle(screen, leaves_color, (xt + 15 * t / 2 - 30 * t, yt - 30 * t + 15 * t), 30 * t)
    circle(screen, leaves_color, (xt + 15 * t / 2 + 30 * t, yt - 30 * t - 20 * t), 30 * t)
    circle(screen, leaves_color, (xt + 15 * t / 2 - 30 * t, yt - 30 * t - 20 * t), 30 * t)
    circle(screen, leaves_color, (xt + 15 * t / 2, yt - 30 * t - 50 * t), 30 * t)


def cloud(screen, xc, yc, c):
    '''
    Рисует облако. Параметры:
    screen - объект pygame.Surface
    xc, yc - координаты
    c - масштаб облака
    '''
    white = (255, 255, 255) # Белый - цвет облака
    circle(screen, white, (xc, yc), 30 * c, 0)
    circle(screen, white, (xc + 30 * c, yc + 30 * c), 30 * c, 0)
    circle(screen, white, (xc + 30 * c, yc - 30 * c), 30 * c, 0)
    circle(screen, white, (xc + 60 * c, yc), 30 * c, 0)
    circle(screen, white, (xc + 90 * c, yc + 30 * c), 30 * c, 0)
    circle(screen, white, (xc + 90 * c, yc - 30 * c), 30 * c, 0)
    circle(screen, white, (xc + 120 * c, yc), 30 * c, 0)


def sun(screen, xs, ys, s):
    '''
    Рисует солнце. Параметры:
    screen - объект pygame.Surface
    xs, ys - координаты центра солнца
    s - масштаб солнца
    '''
    color = (255, 255, 0) #Цвет солнца (жёлтый)
    circle(screen, color, (xs, ys), 30 * s)
    
    
# ОСНОВНАЯ ЧАСТЬ ПРОГРАММЫ
# Начинаем работу в pygame
pygame.init()
# Количество кадров в секунду
FPS = 30
# Создаём окно 500x500 пикселей
screen = pygame.display.set_mode((500, 500))

# Рисуем картинку
rect(screen, (66, 170, 255), (0, 0, 500, 250), 0)  # Небо
rect(screen, (0, 128, 0), (0, 250, 500, 250), 0)  # Трава
home(screen, 50, 270, 1.25)
home(screen, 300, 200, 0.75)
tree(screen, 300, 350, 1)
tree(screen, 450, 230, 0.75)
cloud(screen, 50, 50, 1)
cloud(screen, 230, 80, 0.5)
sun(screen, 450, 50, 1)
cloud(screen, 400, 80, 0.5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

