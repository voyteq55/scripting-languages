from typing import Callable, Any, Generator
import functools, logging
from log_decorator import log


def make_generator(f: Callable[[Any], Any]) -> Generator[Any, None, None]:
    def inner_generator() -> Generator[Any, None, None]:
        current_number = 1
        while True:
            yield f(current_number)
            current_number += 1
    return inner_generator()


def make_generator_mem(f: Callable[[Any], Any]) -> Generator[Any, None, None]:
    @functools.lru_cache()
    def f_mem(arg):
        return f(arg)
    globals()[f.__name__] = f_mem
    return make_generator(f)


@log(logging.DEBUG)
def fibonacci(n: int) -> int:
    previous = 1
    current = 0
    for _ in range(n):
        current, previous = current + previous, current
    return current


def rec_fibonacci(n: int) -> int:
    logging.debug(f"calling recursive fibonacci method for n = {n}")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rec_fibonacci(n - 1) +  rec_fibonacci(n - 2)
