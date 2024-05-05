import logging_setup

import pytest
from typing import List, Dict, Callable, Iterable, Any
from non_imperative_functions import acronym, median, newton_root, make_alpha_dict, flatten
from higher_order_functions import forall, exists, atleast, atmost
from passwordgenerator import PasswordGenerator
from generator_utils import make_generator, make_generator_mem, fibonacci, rec_fibonacci


@pytest.mark.parametrize(
    "strings, expected_result",
    [
        (
            ["Zakład", "Ubezpieczeń", "Społecznych"],
            "ZUS"
        ),
        (
            [],
            ""
        ),
        (
            ["abcd", "" , "efgh", " ", "ijkl"],
            "ae i"
        )

    ]
)
def test_acronym(strings: List[str], expected_result: str):
    assert acronym(strings) == expected_result


@pytest.mark.parametrize(
    "numbers, expected_result",
    [
        (
            [1,1,19,2,3,4,4,5,1],
            3
        ),
        (
            [254],
            254
        ),
        (
            [123,124],
            123.5
        ),
        (
            [100.7, 110, 100],
            100.7
        )
    ]
)
def test_median(numbers: List[float], expected_result: float):
    assert median(numbers) == expected_result


@pytest.mark.parametrize(
    "x, epsilon, expected_y",
    [
        (3, 0.1, 1.75),
        (9, 0.00000000001, 3)
    ]
)
def test_newton_root(x: float, epsilon: float, expected_y: float):
    assert newton_root(x, epsilon) == expected_y


@pytest.mark.parametrize(
    "string, expected_result",
    [
        (
            "on i ona",
            {'o': ['on', 'ona'], 'n': ['on', 'ona'], 'i': ['i'], 'a': ['ona']}
        ),
        (
            "abc aae aaaaacd",
            {'a': ['abc', 'aae', 'aaaaacd'], 'b': ['abc'], 'c': ['abc', 'aaaaacd'], 'd': ['aaaaacd'], 'e': ['aae']}
        ),
        (
            "",
            {}
        ),
        (
            "x",
            {'x': ['x']}
        )
    ]
)
def test_make_alpha_dict(string: str, expected_result: Dict[str, List[str]]):
    assert make_alpha_dict(string) == expected_result


@pytest.mark.parametrize(
    "elements, expected_result",
    [
        (
            [1, [2, 3], [[4, 5], 6]],
            [1, 2, 3, 4, 5, 6]
        ),
        (
            ([([1],), [2]], (3, 4), (5, [[[6], [[7]]]])),
            [1, 2, 3, 4, 5, 6, 7]
        ),
        (
            ([[]],),
            []
        ),
        (
            [1],
            [1]
        )
    ]
)
def test_flatten(elements: list, expected_result: list):
    assert flatten(elements) == expected_result


@pytest.mark.parametrize(
    "pred, iterable, expected_result",
    [
        (
            lambda x: x < 10,
            (i for i in range(10)),
            True
        ),
        (
            lambda x: x % 2 == 0,
            [0, 2, 4, 6, 7],
            False
        ),
        (
            lambda x: False,
            [],
            True
        )
    ]
)
def test_forall(pred: Callable[[Any], bool], iterable: Iterable[Any], expected_result: bool):
    assert forall(pred, iterable) == expected_result


@pytest.mark.parametrize(
    "pred, iterable, expected_result",
    [
        (
            lambda x: x < 10,
            (i for i in range(10)),
            True
        ),
        (
            lambda x: x % 2 == 1,
            [0, 2, 4, 6, 7],
            True
        ),
        (
            lambda x: len(x) > 0,
            ["", "", ""],
            False
        ),
        (
            lambda x: True,
            [],
            False
        )
    ]
)
def test_exists(pred: Callable[[Any], bool], iterable: Iterable[Any], expected_result: bool):
    assert exists(pred, iterable) == expected_result


@pytest.mark.parametrize(
    "n, pred, iterable, expected_result",
    [
        (
            10,
            lambda x: x < 10,
            (i for i in range(10)),
            True
        ),
        (
            11,
            lambda x: x < 10,
            (i for i in range(10)),
            False
        ),
        (
            3,
            lambda x: x % 2 == 1,
            [0, 2, 4, 5, 7],
            False
        ),
        (
            2,
            lambda x: x % 2 == 1,
            [0, 2, 4, 5, 7],
            True
        ),
        (
            1,
            lambda x: True,
            [],
            False
        )
    ]
)
def test_atleast(n: int, pred: Callable[[Any], bool], iterable: Iterable[Any], expected_result: bool):
    assert atleast(n, pred, iterable) == expected_result


@pytest.mark.parametrize(
    "n, pred, iterable, expected_result",
    [
        (
            10,
            lambda x: x < 10,
            (i for i in range(10)),
            True
        ),
        (
            9,
            lambda x: x < 10,
            (i for i in range(10)),
            False
        ),
        (
            3,
            lambda x: x % 2 == 1,
            [0, 2, 4, 5, 7],
            True
        ),
        (
            2,
            lambda x: x % 2 == 1,
            [0, 2, 4, 5, 7],
            True
        ),
        (
            1,
            lambda x: x % 2 == 1,
            [0, 2, 4, 5, 7],
            False
        ),
        (
            1,
            lambda x: True,
            [],
            True
        )
    ]
)
def test_atmost(n: int, pred: Callable[[Any], bool], iterable: Iterable[Any], expected_result: bool):
    assert atmost(n, pred, iterable) == expected_result


def test_default_charset_password_generator():
    pswd_generator = PasswordGenerator(8, 5)
    passwords = [password for password in pswd_generator]
    assert len(passwords) == 5
    for password in passwords:
        print(password)
        assert len(password) == 8


def test_custom_charset_password_generator():
    pswd_generator = PasswordGenerator(10, 6, charset={"a", "b", "c", "1", "2", "3"})
    passwords = [password for password in pswd_generator]
    assert len(passwords) == 6
    for password in passwords:
        print(password)
        assert len(password) == 10


def test_password_generator_explicitly():
    pswd_generator = PasswordGenerator(5, 4) 
    pswd_iterator = iter(pswd_generator)
    passwords = []
    while True:
        try:
            passwords.append(next(pswd_iterator))
        except StopIteration:
            break
    assert len(passwords) == 4
    for password in passwords:
        print(password)
        assert len(password) == 5


def test_make_generator():
    fib_generator = make_generator(fibonacci)
    current_fib_numbers = []
    for fib_number in fib_generator:
        current_fib_numbers.append(fib_number)
        if len(current_fib_numbers) >= 10:
            break
    assert current_fib_numbers == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    geometric_generator = make_generator(lambda x: 2 * 3 ** x)
    current_geometric_sequence = []
    for number in geometric_generator:
        current_geometric_sequence.append(number)
        if len(current_geometric_sequence) >= 5:
            break
    assert current_geometric_sequence == [6, 18, 54, 162, 486]


def test_make_generator_mem():
    fib_mem_generator = make_generator_mem(rec_fibonacci)
    current_fib_numbers = []
    for fib_number in fib_mem_generator:
        current_fib_numbers.append(fib_number)
        if len(current_fib_numbers) >= 10:
            break
    assert current_fib_numbers == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
