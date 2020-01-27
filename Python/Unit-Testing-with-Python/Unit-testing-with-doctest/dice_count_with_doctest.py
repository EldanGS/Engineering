def dice_counts(dice):
    """Make a dictionary of how many of each value are in dice

    >>> dice_counts([1, 2, 2, 3, 3])
    {1: 1, 2: 2, 3: 2, 4: 0, 5: 0, 6: 0}

    The Doctest skip information between Traceback and TypeError.
    >>> dice_counts("1234") #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    TypeError: must be str, not int

    """
    return {x: dice.count(x) for x in range(1, 7)}
