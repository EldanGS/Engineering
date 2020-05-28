"""
https://www.educative.io/courses/software-design-patterns-best-practices/B8nMkqBWONo

Singleton pattern as the name suggests is used to create one and only
instance of a class. There are several examples where only a single instance
of a class should exist and the constraint be enforced. Caches, thread pools,
registries are examples of objects that should only have a single instance.

Its trivial to new-up an object of a class but how do we ensure that only one
object ever gets created? The answer is to make the constructor private of
the class we intend to define as singleton. That way, only the members of the
class can access the private constructor and no one else.

Formally the Singleton pattern is defined as ensuring that only a single
instance of a class exists and a global point of access to it exists.


Вкратце, цель шаблона Singleton заключаются в следующем:
• Обеспечение создания одного и только одного объекта класса
• Предоставление точки доступа для объекта, который является глобальным для программы
• Контроль одновременного доступа к ресурсам, которые являются общими
"""

"""As an example, let's say we want to model the American President's 
official aircraft called "Airforce One" in our software. There can only be 
one instance of Airforce One and a singleton class is the best suited 
representation. 

Below is the code for our singleton class
"""


class AirforceOne:
    _only_instance = None

    def __init__(self):
        if not AirforceOne._only_instance:
            print('__init__ method is called')
        else:
            print('Instance already created:', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls._only_instance:
            cls._only_instance = AirforceOne()
        return cls._only_instance

    def fly(self):
        print("Airforce one is flying...")


if __name__ == '__main__':
    air_force_one = AirforceOne.get_instance()
    # air_force_one.__init__()
    air_force_one.fly()
