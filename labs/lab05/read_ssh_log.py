import configure_logging
from typing import Generator, Optional
from collections import namedtuple
from collections.abc import Iterable
from datetime import datetime
import re, patterns, logging

LogEntry = namedtuple("LogEntry", ["timestamp", "host", "app_comp", "pid", "description"])
date_format = "%b %d %H:%M:%S"


def read_log(filepath: str) -> Generator[str, None, None]:
    with open(filepath) as file:
        for line in file.readlines():
            logging.debug(f"Bytes read from line: {len(line.encode('utf-8'))}")
            yield line


def get_entries(lines: Generator[str, None, None]) -> Generator[LogEntry, None, None]:
    return (nmd_tuple for entry in lines if (nmd_tuple := get_namedtuple_from_entry(entry)))


def get_namedtuple_from_entry(entry: str) -> Optional[LogEntry]:
    if regex_match := re.match(patterns.ENTRY, entry):
        attrs = regex_match.groupdict()
        attrs["timestamp"] = datetime.strptime(attrs["timestamp"], date_format)
        attrs["pid"] = int(attrs["pid"])
        return LogEntry(**attrs)
    return None


if __name__ == "__main__":
    for entry in get_entries(read_log("logs/short.log")):
        print(entry)
