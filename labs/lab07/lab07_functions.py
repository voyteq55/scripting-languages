from typing import List, Dict


def acronym(strings: List[str]) -> str:
    return "".join(map(lambda string: string[0] if string else "", strings))


def median(numbers: List[float]) -> float:
    numbers_count = len(numbers)
    sorted_numbers = sorted(numbers)
    return sorted_numbers[numbers_count // 2] if numbers_count % 2 == 1 else (sorted_numbers[numbers_count // 2 - 1] + sorted_numbers[numbers_count // 2]) / 2


def newton_root(x: float, epsilon: float) -> float:
    def newton_root_inner(current_y: float) -> float:
        return current_y if abs(current_y ** 2 - x) < epsilon else newton_root_inner((current_y + x / current_y) / 2)
    return newton_root_inner(x / 2)


def make_alpha_dict(string: str) -> Dict[str, str]:
    return {letter: [word for word in string.split() if letter in word] for letter in string.replace(" ", "")}


def flatten(elements: list) -> list:
    return [item for subelements in elements for item in (flatten(subelements) if isinstance(subelements, list) or isinstance(subelements, tuple) else [subelements])]