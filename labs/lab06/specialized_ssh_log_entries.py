import sys
sys.path.append('../lab05')

from read_ssh_log import LogEntry, get_namedtuple_from_entry
from log_functions import get_ipv4s_from_log

from sshlogentry import SSHLogEntry
from log_utils import get_port, get_failed_user, get_accepted_user, get_error_type


class FailedPassSSHLogEntry(SSHLogEntry):
    def __init__(self, line: str) -> None:
        super().__init__(line)
        self.port = get_port(self.description)
        self.failed_user = get_failed_user(self.description)

    def validate(self) -> bool:
        if not (entry := get_namedtuple_from_entry(self._SSHLogEntry__raw_entry)):
            return False
        return get_port(entry.description) == self.port and get_failed_user(entry.description) == self.failed_user


class AcceptedPassSSHLogEntry(SSHLogEntry):
    def __init__(self, line: str) -> None:
        super().__init__(line)
        self.port = get_port(self.description)
        self.accepted_user = get_accepted_user(self.description)

    def validate(self) -> bool:
        if not (entry := get_namedtuple_from_entry(self._SSHLogEntry__raw_entry)):
            return False
        return get_port(entry.description) == self.port and get_accepted_user(entry.description) == self.accepted_user


class ErrorSSHLogEntry(SSHLogEntry):
    def __init__(self, line: str) -> None:
        super().__init__(line)
        self.error_type = get_error_type(self.description)

    def validate(self) -> bool:
        if not (entry := get_namedtuple_from_entry(self._SSHLogEntry__raw_entry)):
            return False
        return get_error_type(entry.description) == self.error_type


class OtherSSHLogEntry(SSHLogEntry):
    def __init__(self, line: str) -> None:
        super().__init__(line)

    def validate(self) -> bool:
        return True

