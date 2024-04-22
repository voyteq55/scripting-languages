import configure_logging
import argparse, cmd_names, logging, sys
from read_ssh_log import read_log, get_entries, LogEntry
from log_functions import get_ipv4s_from_log, get_message_type, get_user_from_log
from process_log import get_random_entries_for_random_user, get_connection_durations_for_user, get_most_and_least_frequent_users
from typing import Generator, Iterable
import numpy as np


def get_subcommand_result_stream(cmd_name: str, filepath: str) -> Iterable[str]:
    entries = get_entries(read_log(filepath))
    if cmd_name == cmd_names.IPV4s:
        return get_ipv4s_stream(entries)
    if cmd_name == cmd_names.USER:
        return get_users_stream(entries)
    if cmd_name == cmd_names.MESSAGE_TYPE:
        return get_msg_types_stream(entries)
    if cmd_name == cmd_names.SSH_DURATION:
        return get_duration_avg_global(entries)
    if cmd_name == cmd_names.SSH_DURATION_PER_USER:
        return get_duration_avg_for_users_stream(entries)
    if cmd_name == cmd_names.MOST_AND_LEAST_FREQUENT_USERS:
        return [str(get_most_and_least_frequent_users(entries))]
    print("illegal subcommand", file=sys.stderr)
    exit(1)


def get_ipv4s_stream(entries: Generator[LogEntry, None, None]) -> Generator[str, None, None]:
    return (str(get_ipv4s_from_log(entry)) for entry in entries)


def get_users_stream(entries: Generator[LogEntry, None, None]) -> Generator[str, None, None]:
    return ((user if (user := get_user_from_log(entry)) else str()) for entry in entries)


def get_msg_types_stream(entries: Generator[LogEntry, None, None]) -> Generator[str, None, None]:
    return (get_message_type(entry.description) for entry in entries)


def get_duration_avg_for_users_stream(entries: Generator[LogEntry, None, None]) -> Generator[str, None, None]:
    durations = get_connection_durations_for_user(entries)
    for user in durations:
        durations_in_seconds = [duration.total_seconds() for duration in durations[user]]
        avg = np.mean(durations_in_seconds)
        std_dev = np.std(durations_in_seconds)
        yield f"{user}: average = {avg} seconds, standard deviation = {std_dev} seconds"


def get_duration_avg_global(entries: Generator[LogEntry, None, None]) -> Generator[str, None, None]:
    durations = get_connection_durations_for_user(entries)
    all_durations_in_seconds = [duration.total_seconds() for durations in durations.values() for duration in durations]
    avg = np.mean(all_durations_in_seconds)
    std_dev = np.std(all_durations_in_seconds)
    yield f"average = {avg} seconds, standard deviation = {std_dev} seconds"


def get_parsed_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Script for analysing ssh log files")
    parser.add_argument("--file", required=True, dest="filepath", help="specify a path to a log file")
    parser.add_argument("--log-level", required=False, help="(optional) specify a minimum logging level [DEBUG|INFO|WARNING|ERROR|CRITICAL]")

    subparser = parser.add_subparsers(title="subcommands", dest="cmd_name")
    subparser.add_parser(cmd_names.IPV4s, help="print ipv4 addresses for every line")
    subparser.add_parser(cmd_names.USER, help="print a username for every line (empty string if user not present)")
    subparser.add_parser(cmd_names.MESSAGE_TYPE, help="print a message type for every line")
    random_logs_parser = subparser.add_parser(cmd_names.RANDOM_LOGS_FROM_USER, help="print n random logs for a random user")
    random_logs_parser.add_argument("--n", required=True, help="specify (n) number of logs to print ")
    ssh_duration_parser = subparser.add_parser(cmd_names.SSH_DURATION, help="print average and std deviation of connection duration")
    ssh_duration_parser.add_argument("--per-user", action="store_true", help="(optional) indicate that averages are shown separately for each user")
    subparser.add_parser(cmd_names.MOST_AND_LEAST_FREQUENT_USERS, help="print the most and the least frequent users")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_parsed_args()
    if args.log_level:
        logger = logging.getLogger()
        logger.setLevel(args.log_level)
    if args.cmd_name == cmd_names.RANDOM_LOGS_FROM_USER and args.n:
        result_stream = get_random_entries_for_random_user(read_log(args.filepath), int(args.n))
    else:
        cmd_name = cmd_names.SSH_DURATION_PER_USER if (args.cmd_name == cmd_names.SSH_DURATION and args.per_user) else args.cmd_name
        result_stream = get_subcommand_result_stream(cmd_name, args.filepath)
    for line in result_stream:
        print(line.rstrip())
