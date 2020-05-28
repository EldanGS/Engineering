"""Prototype pattern involves creating new objects by copying existing
objects. The object whose copies are made is called the prototype. You can
think of the prototype object as the seed object from which other objects get
created but you might ask why would we want to create copies of objects,
why not just create them anew? The motivations for prototype objects are as
follows:

* Sometimes creating new objects is more expensive than copying existing objects.

* Imagine a class will only be loaded at runtime and you can't access its
constructor statically. The run-time environment creates an instance of each
dynamically loaded class automatically and registers it with a prototype
manager. The application can request objects from the prototype manager which
in turn can return clones of the prototype.

* The number of classes in a system can be greatly reduced by varying the
values of a cloned object from a prototypical instance.

Formally, the pattern is defined as specify the kind of objects to create
using a prototypical instance as a model and making copies of the prototype
to create new objects.

Шаблон проектирования Prototype решает проблему копирования объектов путем
делегирования этой задачи самим объектам. Все объекты, которые можно
копировать, должны реализовать метод clone и использовать его для получения
точных копий самих себя.

"""

"""Let's take an example to better understand the prototype pattern. We'll 
take up our aircraft example. We created a class to represent the F-16. 
However, we also know that F-16 has a handful of variants. We can subclass 
the F16 class to represent each one of the variants but then we'll end up 
with several subclasses in our system. Furthermore, let's assume that the F16 
variants only differ by their engine types. Then one possibility could be, 
we retain only a single F16 class to represent all the versions of the 
aircraft but we add a setter for the engine. That way, we can create a single 
F16 object as a prototype, clone it for the various versions and compose the 
cloned jet objects with the right engine type to represent the corresponding 
variant of the aircraft. 
"""

from abc import ABC, abstractmethod
from copy import deepcopy


class F16Engine:
    pass


class IAircraftPrototype(ABC):
    def clone(self):
        pass

    def fly(self):
        pass

    def set_engine(self, f16engine):
        pass


class F16(IAircraftPrototype):
    f16engine = None

    def fly(self):
        print("F-16 flying...")

    def __operation__(self):
        self.performed_operation = True

    def clone(self):
        return deepcopy(self)

    def set_engine(self, f16engine):
        F16.f16engine = f16engine


if __name__ == '__main__':
    prototype = F16()

    f16a = prototype.clone()
    f16a.set_engine(F16Engine)

    f16b = prototype.clone()
    f16b.set_engine(F16Engine)

    f16a.fly()
    f16b.fly()

"""Note that the interface IAircraftPrototype clone method returns an 
abstract type. The client doesn't know the concrete subclasses. The Boeing747 
class can just as well implement the same interface and be on its way to 
produce copies of prototypes. The client if passed in the prototype as 
IAircraftPrototype wouldn't know whether the clone's concrete subclass is an 
F16 or a Boeing747. 

The prototype pattern helps eliminate subclassing as the behavior of 
prototype objects can be varied by composing them with subparts. 
"""
