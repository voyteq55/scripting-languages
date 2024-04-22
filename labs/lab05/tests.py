import pytest
import configure_logging
from typing import Optional, List
from datetime import datetime
from read_ssh_log import LogEntry, get_namedtuple_from_entry, read_log, get_entries
from log_functions import get_ipv4s_from_log, get_user_from_log, get_message_type
from process_log import get_most_and_least_frequent_users
import message_type


@pytest.mark.parametrize(
    "entry, expected_tuple",
    [
        (
            "Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]",
            LogEntry(datetime(1900, 12, 10, 7, 2, 47), "LabSZ", "sshd", 24203, "Connection closed by 212.47.254.145 [preauth]")
        ),
        (
            "",
            None
        ),
        (
            "Dec 10 07.02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]",
            None
        )
    ]
)
def test_get_namedtuple_from_entry(entry: str, expected_tuple: Optional[LogEntry]):
    assert get_namedtuple_from_entry(entry) == expected_tuple


@pytest.mark.parametrize(
    "entry, expected_ipv4s",
    [
        (
            LogEntry(None, None, None, None, description=": 127.0.0.1 127.0.0.1 1234123.1231231.23123.123 abc ... 0.0.0.."),
            ["127.0.0.1", "127.0.0.1"]
        ),
        (
            LogEntry(None, None, None, None, ""),
            []
        )
    ]
)
def test_get_ipv4s_from_log(entry: LogEntry, expected_ipv4s: List[str]):
    assert get_ipv4s_from_log(entry) == expected_ipv4s


@pytest.mark.parametrize(
    "entry, expected_user",
    [
        (
            LogEntry(None, None, None, None, description="Invalid user oracle from 187.141.143.180"),
            "oracle"
        ),
        (
            LogEntry(None, None, None, None, description="Received disconnect from 187.141.143.180: 11: Bye Bye [preauth]"),
            None
        ),
        (
            LogEntry(None, None, None, None, description="input_userauth_request: invalid user admin [preauth]"),
            "admin"
        ),
        (
            LogEntry(None, None, None, None, description="pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=112.95.230.3  user=root"),
            "root"
        ),
        (
            LogEntry(None, None, None, None, description="pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=112.95.230.3"),
            None
        ),
        (
            LogEntry(None, None, None, None, description="Received disconnect from 119.137.60.156: 11: disconnected by user"),
            None
        ),
        (
            LogEntry(None, None, None, None, description="Accepted password for fztu from 119.137.60.156 port 56474 ssh2"),
            "fztu"
        )
        
        
    ]
)
def test_get_user_from_log(entry: LogEntry, expected_user: Optional[str]):
    assert get_user_from_log(entry) == expected_user


@pytest.mark.parametrize(
    "description, expected_type",
    [
        (
            "Accepted password for fztu from 119.137.62.142 port 49116 ssh2",
            message_type.SUCCESS
        ),
        (
            "pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=187.141.143.180",
            message_type.FAIL
        ),
        (
            "Connection closed by 5.188.10.180 [preauth]",
            message_type.DISCONNECT
        ),
        (
            "Received disconnect from 119.137.63.195: 11: disconnected by user",
            message_type.DISCONNECT
        ),
        (
            "Failed password for invalid user test from 52.80.34.196 port 36060 ssh2",
            message_type.INVALID_USER
        ),
        (
            "Invalid user oracle from 187.141.143.180",
            message_type.INVALID_USER
        ),
        (
            "Failed password for uucp from 195.154.37.122 port 59266 ssh2",
            message_type.INVALID_PASS,
        ),
        (
            "reverse mapping checking getaddrinfo for customer-187-141-143-180-sta.uninet-ide.com.mx [187.141.143.180] failed - POSSIBLE BREAK-IN ATTEMPT!",
            message_type.BREAKIN
        ),
        (
            "pam_unix(sshd:auth): check pass; user unknown",
            message_type.OTHER
        )
    ]
)
def test_get_message_type(description: str, expected_type: str):
    assert get_message_type(description) == expected_type


def test_get_most_and_least_frequent_users():
    assert get_most_and_least_frequent_users(get_entries(read_log("logs/short.log"))) == ("webmaster", "fztu")
