"""
Для работы программы необходима библиотека PyGame.

Программа запускается из консоли, как обычный Python скрипт:

$ python3 screen.py

В открывшемся окне программы доступны следующие команды управления:

<F1>  - показать справку по командам <R>  - рестарт <P>  - пауза,
снять/поставить <num->  - увеличить количество точек «сглаживания» <num+>  -
уменьшить количество точек «сглаживания» <mouse left>  - добавить «опорную»
точку По умолчанию при старте программы «опорные» точки отсутствуют и
программа находится в состоянии паузы (движение кривой выключено). Для
добавления точек сделайте несколько кликов левой клавишей мыши в любом месте
окна программы. Отрисовка кривой произойдет, когда точек на экране станет
больше двух. Нажмите клавишу <P>, чтобы включить движение кривой.

Ваша задача:

1. Изучить документацию к библиотеке pygame и код программы. Понять механизм
работы программы (как происходит отрисовка кривой, перерасчет точек
сглаживания и другие нюансы реализации программы)

2. Провести рефакторниг кода, переписать программу в ООП стиле с
использованием классов и наследования.

Реализовать класс 2-мерных векторов Vec2d [1]. В классе следует определить
методы для основных математических операций, необходимых для работы с
вектором: Vec2d.__add__ (сумма), Vec2d.__sub__ (разность), Vec2d.__mul__ (
произведение на число). А также добавить возможность вычислять длину вектора
с использованием функции len(a) и метод int_pair, который возвращает кортеж
из двух целых чисел (текущие координаты вектора). Реализовать класс замкнутых
ломаных Polyline с методами отвечающими за добавление в ломаную точки (Vec2d)
c её скоростью, пересчёт координат точек (set_points) и отрисовку ломаной (
draw_points). Арифметические действия с векторами должны быть реализованы с
помощью операторов, а не через вызовы соответствующих методов. Реализовать
класс Knot (наследник класса Polyline), в котором добавление и пересчёт
координат инициируют вызов функции get_knot для расчёта точек кривой по
добавляемым «опорным» точкам [2]. Все классы должны быть самостоятельными и
не использовать внешние функции. Реализовать дополнительный функционал (
выполнение требований этого пункта предоставляет возможность потренировать
свои навыки программирования и позволяет получить дополнительные баллы в этом
задании). К дополнительным задачам относятся: реализовать возможность
удаления «опорной» точки из кривой, реализовать возможность отрисовки на
экране нескольких кривых, реализовать возможность ускорения/замедления
скорости движения кривой(-ых). Примечания.

[1] Вектор определяется координатами x, y — точка конца вектора. Начало
вектора всегда совпадает с центом координат (0, 0).

[2] Здесь стоит уточнить, что стоит различать понятия точек, используемых в
описании задания. Существуют два вида: «опорные» и «сглаживания». Первые
задают положение углов замкнутой ломаной и служат основой для вычисления
вторых. Количество точек «сглаживания» определяет насколько плавными будут
обводы углов ломаной. Вы можете поэкспериментировать с изменением количества
точек сглаживания (см. команды программы) и понаблюдать, как изменяется
отрисовка линии при различных значениях (текущее количество точек
«сглаживания» можно посмотреть на экране справки).

Частые вопросы, возникающие при решении данного задания - FAQ.
Review criteriaменьше
Для получения положительной оценки необходимо:

Реализовать все требуемые классы; Все классы должны быть самостоятельными и
полноценными; Полученный код должен корректно исполняться и сохранить все
возможности предоставленного; Для получения максимальной оценки необходимо
реализовать дополнительные задания. Вариантов их решения много. Вам
необходимо предложить свой.

"""

import pygame
from math import sqrt
import random

SCREEN_DIM = (1024, 768)

"""
Vec2d.__add__ (сумма), Vec2d.__sub__ (разность), Vec2d.__mul__ (
произведение на число)
"""


class Vec2d:
    def __init__(self, x_or_pair, y=None):
        if y is None:
            self.x = x_or_pair[0]
            self.y = x_or_pair[1]
        else:
            self.x = x_or_pair
            self.y = y

    def __add__(self, obj):
        return Vec2d(self.x + obj.x, self.y + obj.y)

    def __sub__(self, obj):
        return Vec2d(self.x - obj.x, self.y - obj.y)

    def _scal_mul(self, obj):
        return self.x * obj.x, self.y * obj.y

    def _vec_mul(self, k):
        return Vec2d(self.x * k, self.y * k)

    def __mul__(self, obj):
        if isinstance(obj, Vec2d):
            return self._scal_mul(obj)
        else:
            return self._vec_mul(obj)

    def __len__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def int_pair(self):
        return int(self.x), int(self.y)


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, point, speed):
        self.points.append(point)
        self.speeds.append(speed)

    def set_points(self):
        for i in range(len(self.points)):
            self.points[i] += self.speeds[i]
            if self.points[i].x > SCREEN_DIM[0] or self.points[i].x < 0:
                self.speeds[i] = Vec2d(- self.speeds[i].x, self.speeds[i].y)
            if self.points[i].y > SCREEN_DIM[1] or self.points[i].y < 0:
                self.speeds[i] = Vec2d(self.speeds[i].x, -self.speeds[i].y)

    def draw_points(self, points, width=3, color=(255, 255, 255)):
        for point in points:
            pygame.draw.circle(gameDisplay, color, point.int_pair(), width)


class Knot(Polyline):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def add_point(self, point, speed):
        super().add_point(point, speed)
        self.get_knot()

    def set_points(self):
        super().set_points()
        self.get_knot()

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self.get_point(points, alpha, deg - 1) * (
                1 - alpha)

    def get_points(self, base_points):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
            res.extend(self.get_points(ptn))
        return res

    def draw_points(self, points, width=3, color=(255, 255, 255)):
        for p_n in range(-1, len(points) - 1):
            pygame.draw.line(gameDisplay, color, points[p_n].int_pair(),
                             points[p_n + 1].int_pair(), width)


def draw_help():
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])
    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == '__main__':
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")
    steps = 35
    working = True
    polyline = Polyline()
    knot = Knot(steps)
    show_help = False
    pause = True
    hue = 0
    color = pygame.Color(0)
    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    polyline = Polyline()
                    knot = Knot(steps)
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                polyline.add_point(Vec2d(event.pos), Vec2d(random.random() * 2,
                                                           random.random() * 2))
                knot.add_point(Vec2d(event.pos),
                               Vec2d(random.random() * 2, random.random() * 2))
        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        polyline.draw_points(polyline.points)
        knot.draw_points(knot.get_knot(), 3, color)
        if not pause:
            polyline.set_points()
            knot.set_points()
        if show_help:
            draw_help()
        pygame.display.flip()
    pygame.display.quit()
    pygame.quit()
    exit(0)
