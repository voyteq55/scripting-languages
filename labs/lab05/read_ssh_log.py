import configure_logging
from typing import Generator, Optional
from collections import namedtuple
from collections.abc import Iterable
from datetime import datetime
import re, patterns, logging, message_type

LogEntry = namedtuple("LogEntry", ["timestamp", "host", "app_comp", "pid", "description"])
date_format = "%b %d %H:%M:%S"


def read_log(filepath: str) -> Generator[str, None, None]:
    with open(filepath) as file:
        for line in file.readlines():
            log_line(line)
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


def log_line(line: str):
    logging.debug(f"Bytes read from line: {len(line.encode('utf-8'))}") 
    entry = get_namedtuple_from_entry(line)
    if entry:
        description = entry.description
        if re.search(patterns.SUCCESS, description):
            logging.info(f"{message_type.SUCCESS} - {description}")
        if re.search(patterns.FAIL, description):
            logging.warning(f"{message_type.FAIL} - {description}")
        if re.search(patterns.DISCONNECT, description):
            logging.info(f"{message_type.DISCONNECT} - {description}")
        if re.search(patterns.INVALID_USER, description):
            logging.error(f"{message_type.INVALID_USER} - {description}")
        if re.search(patterns.INVALID_PASS, description):
            logging.error(f"{message_type.INVALID_PASS} - {description}")
        if re.search(patterns.BREAKIN, description):
            logging.critical(f"{message_type.BREAKIN} - {description}")


if __name__ == "__main__":
    for entry in get_entries(read_log("logs/short.log")):
        print(entry)
