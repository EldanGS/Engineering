
def fizzbuzz(n, additional_rules=None):
    """
    Convert a number to it's name in the game FizzBuzz
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(7, {7: "Whizz"})
    'Whizz'
    >>> fizzbuzz(35, {7: "Whizz"})
    'BuzzWhizz'

    Dummy is usually is None, to set arguments with None.
    """
    answer = ""
    rules = {3: "Fizz", 5: "Buzz"}
    if additional_rules:
        rules.update(additional_rules)
    for divisor in sorted(rules.keys()):
        if n % divisor == 0:
            answer += rules[divisor]
    if not answer:
        answer += str(n)
    return answer
