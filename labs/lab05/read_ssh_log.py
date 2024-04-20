from typing import Generator, Optional
from collections import namedtuple
from datetime import datetime
import re, patterns, logging

LogEntry = namedtuple("LogEntry", ["timestamp", "host", "app_comp", "pid", "description"])
date_format = "%b %d %H:%M:%S"


def read_log(filepath: str) -> Generator[int, None, None]:
    with open(filepath) as file:
        lines = (line for line in file.readlines())
    return lines


def get_namedtuple_from_entry(entry: str) -> Optional[LogEntry]:
    if regex_match := re.match(patterns.ENTRY, entry):
        attrs = regex_match.groupdict()
        attrs["timestamp"] = datetime.strptime(attrs["timestamp"], date_format)
        attrs["pid"] = int(attrs["pid"])
        return LogEntry(**attrs)
    return None

