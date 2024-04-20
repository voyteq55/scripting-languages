from read_ssh_log import LogEntry
import message_type, patterns
from typing import Optional
import re


def get_ipv4s_from_log(entry: LogEntry) -> list[str]:
    description = entry.description
    return re.findall(patterns.IPV4, description) 


def get_user_from_log(entry: LogEntry) -> Optional[str]:
    description = entry.description
    if regex_match := re.search(patterns.USER, description):
        return regex_match.group(1)
    return None


messages = {
    patterns.SUCCESS: message_type.SUCCESS,
    patterns.FAIL: message_type.FAIL,
    patterns.DISCONNECT: message_type.DISCONNECT,
    patterns.INVALID_PASS: message_type.INVALID_PASS,
    patterns.INVALID_USER: message_type.INVALID_USER,
    patterns.BREAKIN: message_type.BREAKIN
}

def get_message_type(description: str) -> str:
    for pattern in messages:
        if re.search(pattern, description):
            return messages[pattern]
    return message_type.OTHER
