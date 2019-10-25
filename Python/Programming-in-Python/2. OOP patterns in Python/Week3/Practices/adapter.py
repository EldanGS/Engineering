"""Класс Light создает в методе __init__ поле заданного размера. За размер
поля отвечает параметр, представляющий из себя кортеж из 2 чисел. Элемент
dim[1] отвечает за высоту карты, dim[0] за ее ширину. Метод set_lights
устанавливает массив источников света с заданными координатами и просчитывает
освещение. Метод set_obstacles устанавливает препятствия аналогичным образом.
Положение элементов задается списком кортежей. В каждом элементе кортежа
хранятся 2 значения: elem[0] -- координата по ширине карты и elem[1] --
координата по высоте соответственно. Метод generate_lights рассчитывает
освещенность с учетом источников и препятствий.

"""


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for _ in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for _ in range(dim[0])] for _ in range(dim[1])]

    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class System:
    def __init__(self):
        self.system_map = self.grid = [[0 for _ in range(30)] for _ in
                                       range(20)]
        self.system_map[5][7] = 1  # Источники света
        self.system_map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.light_map = light_mapper.lighten(self.system_map)


"""
В системе в конструкторе создается двухмерная, карта, на которой источники 
света обозначены как 1, а препятствия как -1. Метод get_lightening принимает 
в качестве аргумента объект, который должен посчитывать освещение. У объекта 
вызывается метод lighten, который принимает карту объектов и источников света 
и возвращает карту освещенности. 

Вам необходимо написать адаптер MappingAdapter. Прототип класса вам дан в 
качестве исходного кода.
"""


class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(dim)
        lights = self._get_points(1, grid)
        self.adaptee.set_lights(lights)
        obstacles = self._get_points(-1, grid)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()

    @staticmethod
    def _get_points(descriptor, grid):
        return [(j, i) for i in range(len(grid)) for j in range(len(grid[0])) if
                grid[i][j] == descriptor]


"""
Список частых ошибок, совершаемых студентами, при решении данного задания.

1. Решение содержит дополнительный или отладочный код. Решение должно 
содержать только реализацию класса MappingAdapter. 

2. Использование сторонних библиотек (например, numpy) приводит к ошибкам 
импорта. В задании можно использовать только модули стандартной библиотеки 
Python. 

3. Изменение сигнатуры метода lighten класса MappingAdapter. Из описания задания -
" У объекта вызывается метод lighten, который принимает карту объектов и 
источников света и ВОЗВРАЩАЕТ карту освещенности". 

Некоторые студенты пишут реализацию класса MappingAdapter таким образом, 
что вызов метода lighten изменяет значения атрибутов, определенных внутри 
класса. 

4. Игнорирование различий в способах хранения данных в системе и классе 
Light. Из описания задания - 

"Класс Light создает в методе __init__ поле заданного размера. За размер поля 
отвечает параметр, представляющий из себя кортеж из 2 чисел. Элемент dim[1] 
отвечает за высоту карты, dim[0] за ее ширину. .... Положение элементов 
задается списком кортежей. В каждом элементе кортежа хранятся 2 значения: 
elem[0] -- координата по ширине карты и elem[1] -- координата по высоте 
соответственно.…". 

Естественное представление двумерного массива в виде вложенных списков, 
как правило такое, что первый индекс отвечает за высоту, а второй за ширину. 
То есть при обращении к массиву arr[5][3] - вернется третий элемент из 5-го 
вложенного списка. В классе Light, исходя из условия задания, индексация в 
массиве получается "перевернутой". Поэтому это нужно учитывать при создании 
dim и списков с координатами источников света и препятствий. Не учет этого 
момента приводит к ошибке грейдера:  Тест 3. При попытке рассчитать освещение 
выбрасывается исключение IndexError. 

5. Использование «map» в качестве имени переменной для хранения объекта 
карты. В стандартной библиотеке Python есть функция с таким же названием. 
Называя переменную так, вы «затираете» встроенную функцию. В данной задаче 
эта ошибка возможно не приведет к side-эффектам, но такая привычка может 
дорого обойтись в реальном проекте. 
"""
