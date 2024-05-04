import pytest
from typing import List, Dict
from lab07_functions import acronym, median, newton_root, make_alpha_dict, flatten

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