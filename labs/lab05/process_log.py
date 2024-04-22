import configure_logging
from typing import Generator, List, Dict, Tuple, Deque
from collections import deque, defaultdict
from read_ssh_log import LogEntry, get_namedtuple_from_entry
from log_functions import get_user_from_log, get_message_type, get_ipv4s_from_log
import message_type, random, datetime


def get_random_user(entries: Deque[str]) -> str:
    users = set()
    for entry in entries:
        if (log := get_namedtuple_from_entry(entry)) and (username := get_user_from_log(log)):
            users.add(username)
    return random.choice(list(users))


def get_random_entries_for_random_user(logs: Generator[str, None, None], number_of_entries: int) -> List[str]:
    logs = deque(logs)
    random_user = get_random_user(logs)
    all_logs_for_user = deque(entry for entry in logs if (nmd_tuple := get_namedtuple_from_entry(entry)) and (user := get_user_from_log(nmd_tuple)) == random_user)
    if number_of_entries >= len(all_logs_for_user):
        return list(all_logs_for_user)
    return random.sample(list(all_logs_for_user), number_of_entries)


def get_connection_durations_for_user(entries: Generator[LogEntry, None, None]) -> Dict[str, List[datetime.timedelta]]:
    durations = defaultdict(list)
    current_host_login_times = {}
    for entry in entries:
        if get_message_type(entry.description) == message_type.SUCCESS:
            current_host_login_times[get_ipv4s_from_log(entry)[0]] = (entry.timestamp, get_user_from_log(entry))
        if get_message_type(entry.description) == message_type.DISCONNECT and (host := get_ipv4s_from_log(entry)[0]) in current_host_login_times:
            login_time, user = current_host_login_times[host]
            durations[user].append(entry.timestamp - login_time)
            current_host_login_times.pop(host)
    return dict(durations)


def get_most_and_least_frequent_users(entries: Generator[LogEntry, None, None]) -> Tuple[str, str]:
    users_count = defaultdict(int)
    for entry in entries:
        if user := get_user_from_log(entry):
            users_count[user] += 1
    most_frequent_user = max(users_count, key=lambda user: users_count[user])
    least_frequent_user = min(users_count, key=lambda user: users_count[user])
    return most_frequent_user, least_frequent_user
