from read_ssh_log import LogEntry
import message_type, patterns
from typing import List, Optional
import re, logging


def get_ipv4s_from_log(entry: LogEntry) -> List[str]:
    description = entry.description
    return re.findall(patterns.IPV4, description) 


def get_user_from_log(entry: LogEntry) -> Optional[str]:
    description = entry.description
    if regex_match := re.search(patterns.USER, description):
        return regex_match.group(1)
    return None


def get_message_type(description: str) -> str:
    if re.search(patterns.SUCCESS, description):
        return message_type.SUCCESS
    if re.search(patterns.FAIL, description):
        return message_type.FAIL
    if re.search(patterns.DISCONNECT, description):
        return message_type.DISCONNECT
    if re.search(patterns.INVALID_USER, description):
        return message_type.INVALID_USER
    if re.search(patterns.INVALID_PASS, description):
        return message_type.INVALID_PASS
    if re.search(patterns.BREAKIN, description):
        return message_type.BREAKIN
    return message_type.OTHER
