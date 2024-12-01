

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the failing test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    assert car.fuel == 0
    car = Car(fuel=10)
    assert car.fuel == 10

def format_as_sentence(phrase):
    """
    >>> format_as_sentence("hello")
    'Hello.'
    >>> format_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_as_sentence("You are good")
    'You are good.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]

# Uncomment the following line to enable the doctest to run
doctest.testmod()

run_tests()

