from typing import Iterable, Iterator
import string, random, logging
from log_decorator import log


DEFAULT_CHARS = list(string.ascii_letters + string.digits)


@log(logging.CRITICAL)
class PasswordGenerator:
    def __init__(self, length: int, count: int, charset: Iterable[str] = DEFAULT_CHARS) -> None:
        self.current_index = 0
        self.length = length
        self.charset = list(charset)
        self.count = count

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        if self.current_index >= self.count:
            raise StopIteration
        self.current_index += 1
        return "".join(random.choice(self.charset) for _ in range(self.length))
