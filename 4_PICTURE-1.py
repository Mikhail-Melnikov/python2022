import pygame
from pygame.draw import *
import math

pygame.init()

def angled_ellipse(
        surface, color, rect, angle, width=0, border_color=(255, 255, 255)):
    '''
    Рисует наклоненный на заданный угол закрашенный эллипс

    Parameters
    ----------
    surface : объект pygame.Surface
        Поверхость, на которой происходит рисование.
    color : Кортеж RGB
        Цвет эллипса.
    rect : Четырехэлементный кортеж
        Координаты описаннного около эллипса прямоугольника.
    angle : Число
        Угол наклона (в градусах).
    width : Число, optional
        Толщина окаймления эллипса. The default is 0.
    border_color : Кортеж RGB, optional
        Цвет окаймления эллипса. The default is (255, 255, 255).
    Returns
    -------
    Выводит закрашенный эллипс с заданными характеристиками на экран.

    '''

    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size))
    pygame.draw.ellipse(
        shape_surf, border_color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(
        center=target_rect.center))

def window(x, y, a, b, w):
    rect(screen, (135, 205, 222), (x, y, a, b))
    rect(screen, (213, 255, 230), (x, y, a, w))
    rect(screen, (213, 255, 230), (x, y + b, a + w, w))
    rect(screen, (213, 255, 230), (x, y, w, b))
    rect(screen, (213, 255, 230), (x + a, y, w, b))
    rect(screen, (213, 255, 230), (x + a//2, y, w, b))
    rect(screen, (213, 255, 230), (x, y + b//2 - w//2, a, w))
    
def cat(x, y, body, eye, size):
    #Хвост
    angled_ellipse(screen, body, (x + size//2, y + size//8, size//4, size//10), 150, 1, (0, 0, 0))
    
    #Тело
    ellipse(screen, body, (x + size // 10, y, size // 2, size // 3.5))
    ellipse(screen, (0, 0, 0), (x + size // 10, y, size // 2, size // 3.5), 1)
    
    #Дальняя нога
    ellipse(screen, body, (x + size // 2.5, y + size // 7, size // 5, size // 5.5))
    ellipse(screen, (0, 0, 0), (x + size // 2.5, y + size // 7, size // 5, size // 5.5), 1)
    ellipse(screen, body, (x + size // 2.5 + size // 7, y + size // 7 + size // 9, size // 15, size // 6))
    ellipse(screen, (0, 0, 0), (x + size // 2.5 + size // 7, y + size // 7 + size // 9, size // 15, size // 6), 1)
    
    #Ближняя нога
    ellipse(screen, body, (x + size // 15, y + size // 5, size // 6, size // 15))
    ellipse(screen, (0, 0, 0), (x + size // 15, y + size // 5, size // 6, size // 15), 1)
    
    #Вообще ближняя нога жестб
    ellipse(screen, body, (x + size // 20, y + size // 15, size // 18, size // 7))
    ellipse(screen, (0, 0, 0), (x + size // 20, y + size // 15, size // 18, size // 7), 1)
    
    #Голова
    ellipse(screen, body, (x, y, size // 5, size // 5.5))
    ellipse(screen, (0, 0, 0), (x, y, size // 5, size // 5.5), 1)
    
    #Глаза
    ellipse(screen, eye, (x + size // 40, y + size // 18, size // 20, size // 18))
    ellipse(screen, eye, (x + size // 5 - 3 * size // 40, y + size // 18, size // 20, size // 18))
    
    ellipse(screen, (0, 0, 0), (x + size // 40, y + size // 18, size // 20, size // 18), 1)
    ellipse(screen, (0, 0, 0), (x + size // 5 - 3 * size // 40, y + size // 18, size // 20, size // 18), 1)
    
    ellipse(screen, (0, 0, 0), (x + 2 * size // 40, y + size // 18, size // 100, size // 20))
    ellipse(screen, (0, 0, 0), (x + size // 5 - 2 * size // 40, y + size // 18, size // 100, size // 20))
    
    angled_ellipse(screen, (255, 255, 255), (x + size // 40 + size // 100, y + size // 18 + size // 80, size // 40, size // 100), 120)
    angled_ellipse(screen, (255, 255, 255), (x + size // 5 - 3 * size // 40 + size // 100, y + size // 18 + size // 80, size // 40, size // 100), 120)
    
    
    #Левое ухо
    polygon(screen, body, [(x - size//100 - 5, y - size//50 - 10), (x + size//40 + 10, y + size//40 + 5), (x + size//100 - 5, y + size//20 + 10)])
    polygon(screen, (0, 0, 0), [(x - size//100 - 5, y - size//50 - 10), (x + size//40 + 10, y + size//40 + 5), (x + size//100 - 5, y + size//20 + 10)], 1)
    polygon(screen, (222, 170, 135), [(x - size//100, y - size//50), (x + size//40, y + size//40), (x + size//100, y + size//20)])
    polygon(screen, (0, 0, 0), [(x - size//100, y - size//50), (x + size//40, y + size//40), (x + size//100, y + size//20)], 1)
    
    #Правое ухо
    polygon(screen, body, [( 2 * x + size // 5 - (x - size//100 - 5), y - size//50 - 10), (2 * x + size // 5 - (x + size//40 + 10), y + size//40 + 5), (2 * x + size // 5 - (x + size//100 - 5), y + size//20 + 10)])
    polygon(screen, (0, 0, 0), [( 2 * x + size // 5 - (x - size//100 - 5), y - size//50 - 10), (2 * x + size // 5 - (x + size//40 + 10), y + size//40 + 5), (2 * x + size // 5 - (x + size//100 - 5), y + size//20 + 10)], 1)
    polygon(screen, (222, 170, 135), [(2*x + size//5 - (x - size//100), y - size//50), (2*x + size//5 - (x + size//40), y + size//40), (2*x + size//5 - (x + size//100), y + size//20)])
    polygon(screen, (0, 0, 0), [(2*x + size//5 - (x - size//100), y - size//50), (2*x + size//5 - (x + size//40), y + size//40), (2*x + size//5 - (x + size//100), y + size//20)], 1)
    
    #Нос
    polygon(screen, (255, 204, 170), [(x + size//10 - size//100, y + size // 9), (x + size//10 + size//100, y + size // 9), (x + size//10, y + size // 9 + size // 75)])
    polygon(screen, (0, 0, 0), [(x + size//10 - size//100, y + size // 9), (x + size//10 + size//100, y + size // 9), (x + size//10, y + size // 9 + size // 75)], 1)
    
    #Носорот
    line(screen, (0, 0, 0), (x + size//10, y + size // 9 + size // 75), (x + size//10, y + size // 9 + size // 75 + size // 50), 1)
    
    #Рот
    arc(screen, (0, 0, 0), (x + size//10, y + size // 9 + size // 75 + size // 50 - size//100, size // 50, size // 50), math.pi, 2*math.pi, 1)
    arc(screen, (0, 0, 0), (x + size//10 - size//50, y + size // 9 + size // 75 + size // 50 - size//100, size // 50, size // 50), math.pi, 2*math.pi, 1)
    
    #Правые усы
    line(screen, (0, 0, 0), (x + size//10 + size//50, y + size//8), (x + size//10 + size//50 + size//15, y + size//8 - size//50))
    line(screen, (0, 0, 0), (x + size//10 + size//50, y + size//8 + size//200), (x + size//10 + size//50 + size//15, y + size//8 + size//200))
    line(screen, (0, 0, 0), (x + size//10 + size//50, y + size//8 + size//100), (x + size//10 + size//50 + size//15, y + size//8 + size//100 + size//50))
    
    #Левые усы
    line(screen, (0, 0, 0), (x + size//10 - size//50, y + size//8), (x + size//10 - size//50 - size//15, y + size//8 - size//50))
    line(screen, (0, 0, 0), (x + size//10 - size//50, y + size//8 + size//200), (x + size//10 - size//50 - size//15, y + size//8 + size//200))
    line(screen, (0, 0, 0), (x + size//10 - size//50, y + size//8 + size//100), (x + size//10 - size//50 - size//15, y + size//8 + size//100 + size//50))
    
    
def ball(x, y, size):
    circle(screen, (153, 153, 153), (x, y), size)
    circle(screen, (0, 0, 0), (x, y), size, 1)
    line(screen, (0, 0, 0), (x - size//4, y - 3*size // 4), (x + 2*size//4, y - size//4))
    line(screen, (0, 0, 0), (x - size//4, y - 3*size // 4 + size//5), (x + 2*size//4, y - size//4 + size//5))
    line(screen, (0, 0, 0), (x - size//4, y - 3*size // 4 + 2*size//5), (x + 2*size//4, y - size//4 + 2*size//5))
    
    
    

    

FPS = 30
screen = pygame.display.set_mode((600, 800))
#rect(screen, (color), (position, size))
#polygon(screen, (color), [(position)])
#circle(screen, (color), (position), r, <width>)
rect(screen, (85, 68, 0), (0, 0, 600, 400))
rect(screen, (128, 102, 0), (0, 400, 600, 400))
window(250, 20, 200, 350, 20)
cat(50, 450, (200, 113, 55), (136, 170, 0), 600)
ball(500, 700, 50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()