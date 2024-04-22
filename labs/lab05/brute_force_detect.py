from typing import Generator, List, Deque
from collections import defaultdict
from read_ssh_log import LogEntry, read_log, get_entries
from log_functions import get_message_type, get_ipv4s_from_log, get_user_from_log
import message_type, typer
from typing_extensions import Annotated


ALLOWED_LOGIN_ATTEMPTS = 50
DEFAULT_MAX_INTERVAL_SECONDS = 300


def detect_brute_force(entries: Generator[LogEntry, None, None], max_interval_seconds: int, single_user: bool = False) -> List[str]:
    potential_attacks = defaultdict(Deque[LogEntry])
    confirmed_attacks = defaultdict(Deque[LogEntry])
    for entry in entries:
        msg_type = get_message_type(entry.description)
        if (msg_type == message_type.FAIL or msg_type == message_type.INVALID_PASS or msg_type == message_type.INVALID_USER) and (ipv4s := get_ipv4s_from_log(entry)):
            if not (user := get_user_from_log(entry)) and single_user:
                continue
            ip_addr = ipv4s[0]
            identifier = (ip_addr, user) if single_user else ip_addr
            if identifier in confirmed_attacks:
                confirmed_attacks[identifier].append(entry)
            else:
                potential_attacks[identifier].append(entry)
                while (entry.timestamp - potential_attacks[identifier][0].timestamp).total_seconds() > max_interval_seconds:
                    potential_attacks[identifier].popleft()
                if len(potential_attacks[identifier]) > ALLOWED_LOGIN_ATTEMPTS:
                    confirmed_attacks[identifier] = potential_attacks[identifier]
                    del potential_attacks[identifier]
    return [f"brute force attempt starting at {confirmed_attacks[id][0].timestamp}: {id} - {len(confirmed_attacks[id])} attempts" for id in confirmed_attacks]


def main(file: str, max_secs: Annotated[int, typer.Option()] = DEFAULT_MAX_INTERVAL_SECONDS, single_user: Annotated[bool, typer.Option()] = False):
    entries = get_entries(read_log(file))
    for attack in detect_brute_force(entries, max_secs, single_user):
        print(attack)


if __name__ == "__main__":
    typer.run(main)
