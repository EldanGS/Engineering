"""
Необходимо написать комплект тестов используя модуль unittest стандартной библиотеки Python. Имя тестового класса - TestFactorize.

Описание тестов:

test_wrong_types_raise_exception - проверяет, что передаваемый в функцию аргумент типа float или str вызывает
исключение TypeError. Тестовый набор входных данных:  'string',  1.5

test_negative - проверяет, что передача в
функцию factorize отрицательного числа вызывает исключение ValueError. Тестовый набор входных данных:   -1,  -10,
-100

test_zero_and_one_cases - проверяет, что при передаче в функцию целых чисел 0 и 1, возвращаются соответственно
кортежи (0,) и (1,). Набор тестовых данных: 0 → (0, ),  1 → (1, )

test_simple_numbers - что для простых чисел
возвращается кортеж, содержащий одно данное число. Набор тестовых данных: 3 → (3, ),  13 → (13, ),   29 → (29,
)

test_two_simple_multipliers — проверяет случаи, когда передаются числа для которых функция factorize возвращает
кортеж с числом элементов равным 2. Набор тестовых данных: 6 → (2, 3),   26 → (2, 13),   121 --> (11,
11)

test_many_multipliers - проверяет случаи, когда передаются числа для которых функция factorize возвращает кортеж
с числом элементов больше 2. Набор тестовых данных: 1001 → (7, 11, 13) ,   9699690 → (2, 3, 5, 7, 11, 13, 17, 19)

ВАЖНО!  Все входные данные должны быть такими, как указано в условии.
Название переменной в каждом тестовом случае должно быть именно "x".
При этом несколько различных проверок в рамках одного теста должны быть обработаны как подслучаи с указанием x: subTest(x=...).
В задании необходимо реализовать ТОЛЬКО класс TestFactorize, кроме этого реализовывать ничего не нужно.
Импортировать unittest и вызывать unittest.main() в решении также не нужно.
"""

import unittest


def is_not_negative(x):
    return x >= 0


def is_integer(x):
    return isinstance(x, int)


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    if not is_not_negative(x):
        raise ValueError
    if not is_integer(x):
        raise TypeError

    if x == 0 or x == 1:
        return x,

    result = []
    while x % 2 == 0:
        result.append(2)
        x //= 2

    for i in range(3, int(x ** 0.5) + 1, 2):
        while x % i == 0:
            result.append(i)
            x //= i
    if x > 2:
        result.append(x)

    return tuple(result)


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        for x in ('string', 1.5):
            with self.subTest(x=x):
                with self.assertRaises(TypeError):
                    factorize(x)

    def test_negative(self):
        for x in [-1, -10, -100]:
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    factorize(x)

    def test_zero_and_one_cases(self):
        for x in (0, 1):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_simple_numbers(self):
        for x in (3, 13, 29):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_two_simple_multipliers(self):
        with self.subTest(x=6):
            self.assertEqual(factorize(6), (2, 3))
        with self.subTest(x=26):
            self.assertEqual(factorize(26), (2, 13))
        with self.subTest(x=121):
            self.assertEqual(factorize(121), (11, 11))

    def test_many_multipliers(self):
        with self.subTest(x=1001):
            self.assertEqual(factorize(1001), (7, 11, 13))
        with self.subTest(x=9699690):
            self.assertEqual(factorize(9699690), (2, 3, 5, 7, 11, 13, 17, 19))


if __name__ == '__main__':
    unittest.main()
