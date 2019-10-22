"""
Парадигма инкапсуляции
Парадигма инкапсуляции предлагает объединять переменные и методы, относящиеся к одному объекту в единый компонент. По
сути соблюдение парадигмы инкапсуляции и заключается в создании классов.


Парадигма полиморфизма
Парадигма полиморфизма позволяет вместо объекта базового типа использовать его потомка, при этом не указывая это явно.
"""


class Parent:

    def some_method(self):
        print("This is Parent object")


class Child1(Parent):

    def some_method(self):
        print("This is Child1 object")


class Child2(Parent):

    def some_method(self):
        print("This is Child2 object")


def who_am_i(obj):
    obj.some_method()


p = Parent()
c1 = Child1()
c2 = Child2()

who_am_i(p)
who_am_i(c1)
who_am_i(c2)
print()