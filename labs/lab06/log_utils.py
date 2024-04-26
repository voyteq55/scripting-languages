import re


re_port = re.compile(r" port (\d+) ")
re_failed_user = re.compile(r"^Failed password for ([^\s]+) ")
re_accepted_user = re.compile(r"^Accepted password for ([^\s]+) ")
re_error_type = re.compile(r"^error: .*\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}: (.*)$")


def get_port(description: str) -> int:
    if regex_match := re_port.search(description):
        return int(regex_match.group(1))
    return None


def get_failed_user(description: str) -> str:
    if regex_match := re_failed_user.search(description):
        return regex_match.group(1)
    return None


def get_accepted_user(description: str) -> str:
    if regex_match := re_accepted_user.search(description):
        return regex_match.group(1)
    return None


def get_error_type(description: str) -> str:
    if regex_match := re_error_type.search(description):
        return regex_match.group(1)
    return None

