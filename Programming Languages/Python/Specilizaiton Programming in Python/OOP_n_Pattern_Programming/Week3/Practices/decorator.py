"""Представьте себя ненадолго разработчиком компьютерной игры в стиле
фэнтези. Вам поручено написать реализацию системы эффектов, которые могут
быть наложены на героя вашей игры.

В игре есть герой, который обладает некоторым набором характеристик.
Класс героя описан следующим образом:
"""
from abc import ABC, abstractmethod


class HeroCharacter(ABC):

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class Hero(HeroCharacter):
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


"""
К основным характеристикам относятся: Сила (Strength), Восприятие (
Perception), Выносливость (Endurance), Харизма (Charisma), Интеллект (
Intelligence), Ловкость (Agility), Удача (Luck). 

Враги и союзники могут накладывать на героя положительные и отрицательные 
эффекты. Эти эффекты изменяют характеристики героя,  увеличивая или уменьшая 
значения определенных характеристик, в зависимости от того какие эффекты были 
наложены.  На героя можно накладывать бесконечно много эффектов, действие 
одинаковых эффектов суммируется. Игрок должен знать, какие положительные и 
какие отрицательные эффекты на него были наложены и в каком порядке. Названия 
эффектов совпадают с названиями классов. 

За получение данных о текущем состоянии героя отвечают методы get_stats, 
get_positive_effects,  get_negative_effects. 


Описание эффектов:

* Берсерк (Berserk) - Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;
уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
количество единиц здоровья увеличивается на 50.
* Благословение (Blessing) - увеличивает все основные характеристики на 2.
* Слабость (Weakness) - уменьшает характеристики: Сила, Выносливость, Ловкость на 4.
* Сглаз (EvilEye) - уменьшает  характеристику Удача на 10.
* Проклятье (Curse) - уменьшает все основные характеристики на 2.
 

При выполнении задания необходимо учитывать, что:
изначальные характеристики базового объекта не должны меняться. изменения 
характеристик и накладываемых эффектов (баффов/дебаффов) должны происходить 
динамически, то есть вычисляться при вызове методов get_stats, 
get_positive_effects, get_negative_effects абстрактные классы 
AbstractPositive,  AbstractNegative и соответственно их потомки могут 
принимать любой параметр base при инициализации объекта (_ _ init _ _ (self, 
base)) эффекты должны корректно сниматься, в том числе и из середины стека 
"""


class AbstractEffect(Hero, ABC):

    def __init__(self, base):
        super().__init__()
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects

    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):
    """
    Берсерк (Berserk) -
    * Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;
    * Уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
    * Здоровья увеличивается на 50.
    """

    def get_stats(self):
        """
        "HP": # health points
        "MP": # magic points,
        "SP": # skill points
        "Strength":  # сила
        "Perception": # восприятие
        "Endurance": # выносливость
        "Charisma": # харизма
        "Intelligence": # интеллект
        "Agility": # ловкость
        "Luck": # удача
        """
        stats = self.base.get_stats()
        stats["HP"] += 50
        stats["Strength"] += 7
        stats["Endurance"] += 7
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["Perception"] -= 3
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Berserk"]


class Blessing(AbstractPositive):
    """
    Благословение (Blessing) - увеличивает все основные характеристики на 2.
    К основным характеристикам относятся: Сила (Strength), Восприятие (
    Perception), Выносливость (Endurance), Харизма (Charisma), Интеллект (
    Intelligence), Ловкость (Agility), Удача (Luck).
    """

    def get_stats(self):
        """
        "Strength": # сила
        "Perception": # восприятие
        "Endurance": # выносливость
        "Charisma": # харизма
        "Intelligence": # интеллект
        "Agility": # ловкость
        "Luck": # удача
        """
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Perception"] += 2
        stats["Endurance"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2

        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Blessing"]


class AbstractNegative(AbstractEffect):

    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Weakness(AbstractNegative):
    """
    Слабость (Weakness) -
    * Уменьшает характеристики: Сила, Выносливость, Ловкость на 4.
    """

    def get_stats(self):
        """
        "Strength":  # сила
        "Perception": # восприятие
        "Endurance": # выносливость
        "Charisma": # харизма
        "Intelligence": # интеллект
        "Agility": # ловкость
        "Luck": # удача
        """
        stats = self.base.get_stats()
        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Weakness"]


class EvilEye(AbstractNegative):
    """
    Сглаз (EvilEye) - уменьшает  характеристику Удача/Luck на 10.
    """

    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["EvilEye"]


class Curse(AbstractNegative):
    """
    Проклятье (Curse) - уменьшает все основные характеристики на 2.
    """

    def get_stats(self):
        """
        "Strength": # сила
        "Perception": # восприятие
        "Endurance": # выносливость
        "Charisma": # харизма
        "Intelligence": # интеллект
        "Agility": # ловкость
        "Luck": # удача
        """
        stats = self.base.get_stats()
        stats["Strength"] -= 2
        stats["Perception"] -= 2
        stats["Endurance"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Curse"]


"""
if __name__ == '__main__':
    # создадим героя
    hero = Hero()
    # проверим правильность характеристик по-умолчанию
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    # проверим список отрицательных эффектов
    assert hero.get_negative_effects() == []
    # проверим список положительных эффектов
    assert hero.get_positive_effects() == []
    # наложим эффект Berserk
    brs1 = Berserk(hero)
    # проверим правильность изменения характеристик
    assert brs1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 22,
                                'Perception': 1,
                                'Endurance': 15,
                                'Charisma': -1,
                                'Intelligence': 0,
                                'Agility': 15,
                                'Luck': 8}
    # проверим неизменность списка отрицательных эффектов
    assert brs1.get_negative_effects() == []
    # проверим, что в список положительных эффектов был добавлен Berserk
    assert brs1.get_positive_effects() == ['Berserk']
    # повторное наложение эффекта Berserk
    brs2 = Berserk(brs1)
    # наложение эффекта Curse
    cur1 = Curse(brs2)
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 228,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 27,
                                'Perception': -4,
                                'Endurance': 20,
                                'Charisma': -6,
                                'Intelligence': -5,
                                'Agility': 20,
                                'Luck': 13}
    # проверим правильность добавления эффектов в список положительных эффектов
    assert cur1.get_positive_effects() == ['Berserk',
                                           'Berserk'], cur1.get_positive_effects()
    # проверим правильность добавления эффектов в список отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # снятие эффекта Berserk
    cur1.base = brs1
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 20,
                                'Perception': -1,
                                'Endurance': 13,
                                'Charisma': -3,
                                'Intelligence': -2,
                                'Agility': 13,
                                'Luck': 6}
    # проверим правильность удаления эффектов из списка положительных эффектов
    assert cur1.get_positive_effects() == ['Berserk']
    # проверим правильность эффектов в списке отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # проверим незменность характеристик у объекта hero
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    print('All tests - OK!')
"""
