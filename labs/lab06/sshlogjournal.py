from sshlogentry import SSHLogEntry
from typing import Iterator
from ipaddress import IPv4Address
from datetime import datetime
from specialized_ssh_log_entries import get_specialized_ssh_log_entry


class SSHLogJournal:
    def __init__(self) -> None:
        self.entries = []

    def __len__(self) -> int:
        return len(self.entries)

    def __iter__(self) -> Iterator[SSHLogEntry]:
        return iter(self.entries)

    def __contains__(self, entry: SSHLogEntry) -> bool:
        return entry in self.entries

    def append(self, line: str) -> None:
        entry = get_specialized_ssh_log_entry(line)
        if entry.validate():
            self.entries.append(entry)

    def get_entries_with_ip(self, ipv4: IPv4Address) -> Iterator[SSHLogEntry]:
        return filter(lambda entry: entry.ipv4() == ipv4, self.entries)
    
    def get_entries_with_datetime(self, timestamp: datetime) -> Iterator[SSHLogEntry]:
        return filter(lambda entry: entry.timestamp == timestamp, self.entries)

    def __getitem__(self, key):
        if isinstance(key, int) or isinstance(key, slice):
            return self.entries[key]
        if isinstance(key, IPv4Address):
            return self.get_entries_with_ip(key)
        if isinstance(key, datetime):
            return self.get_entries_with_datetime(key)
        raise TypeError(f"key of type {type(key)} is not valid")
