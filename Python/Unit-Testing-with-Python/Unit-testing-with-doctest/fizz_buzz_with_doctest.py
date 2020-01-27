def fizz_buzz(n: int):
    """The FizzBuzz game with couple of examples.
    >>> fizz_buzz(n=5)
    [1, 2, 'Fizz', 4, 'Buzz']
    >>> fizz_buzz(n=10)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']

    Checking if intervals is empty
    >>> fizz_buzz(n=0)
    []

    Incorrect examples to checking doctest to warning
    # >>> fizz_buzz(n="abc")
    []
    # >>> fizz_buzz(n=100)
    []

    """
    fizzbuzz_list = []
    for num in range(1, n + 1):
        if num % 3 == 0:
            fizzbuzz_list.append('Fizz')
        elif num % 5 == 0:
            fizzbuzz_list.append('Buzz')
        elif num % 3 == 0 and num % 5 == 0:
            fizzbuzz_list.append('Fizz Buzz')
        else:
            fizzbuzz_list.append(num)

    return fizzbuzz_list
