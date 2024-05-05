from typing import Callable, Any, Iterable


def forall(pred: Callable[[Any], bool], iterable: Iterable[Any]) -> bool:
    for element in iterable:
        if not pred(element):
            return False
    return True


def exists(pred: Callable[[Any], bool], iterable: Iterable[Any]) -> bool:
    for element in iterable:
        if pred(element):
            return True
    return False


def atleast(n: int, pred: Callable[[Any], bool], iterable: Iterable[Any]) -> bool:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return sum(1 for element in iterable if pred(element)) >= n


def atmost(n: int, pred: Callable[[Any], bool], iterable: Iterable[Any]) -> bool:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return sum(1 for element in iterable if pred(element)) <= n
