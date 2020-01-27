import random


def yatzy_game(number_of_dice: int = 5):
    """
    Roll the indicated number of 6 sided dice using random number generator
    :param number_of_dice: integer
    :return: sorted list
    Using random.seed to hold randomness result

    >>> random.seed(1234)
    >>> yatzy_game(4)
    [1, 1, 1, 4]

    >>> random.seed(5)
    >>> yatzy_game(5)
    [3, 3, 5, 6, 6]

    """
    return sorted(random.choice((1, 2, 3, 4, 5, 6))
                  for _ in range(number_of_dice))
