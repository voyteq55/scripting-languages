ENTRY = (
    r"(?P<timestamp>[A-Z][a-z]{2}\s\d{1,2}\s\d{2}:\d{2}:\d{2})\s" +
    r"(?P<host>[^\s]+)\s" +
    r"(?P<app_comp>[^\s\[]+)" +
    r"\[(?P<pid>\d+)\]:\s"
    r"(?P<description>.*)$"
)
IPV4 = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
USER = r"(?:Accepted password for | user[ =])([^\s]+)"
SUCCESS = r"^Accepted password"
FAIL = r" authentication failure"
DISCONNECT = r"^(Connection closed|Received disconnect )"
INVALID_USER = r"[Ii]nvalid user"
INVALID_PASS = r"^Failed password(?! for invalid user)"
BREAKIN = r"failed - POSSIBLE BREAK-IN ATTEMPT!$"
