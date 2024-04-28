import sys
sys.path.append('../lab05')

from read_ssh_log import LogEntry, get_namedtuple_from_entry
from log_functions import get_ipv4s_from_log

import abc
from typing import Optional
from ipaddress import IPv4Address, AddressValueError

class SSHLogEntry(metaclass=abc.ABCMeta):
    def __init__(self, line: str) -> None:
        entry = get_namedtuple_from_entry(line)
        self.__raw_entry = line.rstrip()
        self.entry = entry
        self.timestamp = entry.timestamp
        self.host = entry.host
        self.pid = entry.pid
        self.description = entry.description

    def __str__(self) -> str:
        return self.__raw_entry
    
    def ipv4(self) -> Optional[IPv4Address]:
        if ipv4s := get_ipv4s_from_log(self.entry):
            try:
                ipv4_addr = IPv4Address(ipv4s[0])
                return ipv4_addr
            except AddressValueError:
                return None
        return None

    @abc.abstractmethod
    def validate(self) -> bool:
        pass

    @property
    def has_ip(self) -> bool:
        return self.ipv4() is not None
    
    def __repr__(self) -> str:
        return f"Instance of type {type(self)}: {self.__raw_entry}"

    def __eq__(self, other: object) -> bool:
        if type(self) != type(other):
            return False
        return self.__raw_entry == other.__raw_entry
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, SSHLogEntry):
            raise TypeError(f"< operator not allowed for instances of {type(self)} and {type(other)}")
        return self.timestamp < other.timestamp

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, SSHLogEntry):
            raise TypeError(f"< operator not allowed for instances of {type(self)} and {type(other)}")
        return self.timestamp > other.timestamp
