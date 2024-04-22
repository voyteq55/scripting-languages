import configure_logging
import typer, logging
import numpy as np
from typing_extensions import Annotated
from read_ssh_log import get_entries, read_log
from log_functions import get_ipv4s_from_log, get_message_type, get_user_from_log
from process_log import get_message_type, get_most_and_least_frequent_users, get_connection_durations_for_user, get_random_entries_for_random_user

app = typer.Typer()
state = {"file": None, "log_level": None}


@app.command()
def ipv4s():
    entries = get_entries(read_log(state["file"]))
    for entry in entries:
        print(str(get_ipv4s_from_log(entry)))


@app.command()
def user():
    entries = get_entries(read_log(state["file"]))
    for entry in entries:
        if user := get_user_from_log(entry):
            print(user)
        else:
            print(str())


@app.command()
def msg_type():
    entries = get_entries(read_log(state["file"]))
    for entry in entries:
        print(get_message_type(entry.description))


@app.command()
def random(n: Annotated[int, typer.Option()] = 10):
    logs = read_log(state["file"])
    for log in get_random_entries_for_random_user(logs, n):
        print(log.rstrip())


@app.command()
def ssh_duration(per_user: Annotated[bool, typer.Option()] = False):
    entries = get_entries(read_log(state["file"]))
    durations = get_connection_durations_for_user(entries)
    if per_user:
        for user in durations:
            durations_in_seconds = [duration.total_seconds() for duration in durations[user]] 
            avg = np.mean(durations_in_seconds)
            std_dev = np.std(durations_in_seconds)
            print(f"{user}: average = {avg} seconds, standard deviation = {std_dev} seconds")
    else:
        durations_in_seconds = [duration.total_seconds() for durations in durations.values() for duration in durations]
        avg = np.mean(durations_in_seconds)
        std_dev = np.std(durations_in_seconds)
        print(f"average = {avg} seconds, standard deviation = {std_dev} seconds")


@app.command()
def freq_user():
    entries = get_entries(read_log(state["file"]))
    print(str(get_most_and_least_frequent_users(entries)))


@app.callback()
def main(file: Annotated[str, typer.Option()], log_level: Annotated[str, typer.Option()] = "ERROR"):
    state["file"] = file 
    logging.getLogger().setLevel(log_level)


if __name__ == "__main__":
    app()
