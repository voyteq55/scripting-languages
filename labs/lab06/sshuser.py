from datetime import datetime
import re


re_username = re.compile(r"^[a-z_][a-z0-9_-]{0,31}$")


class SSHUser:
    def __init__(self, username: str, last_logged: datetime) -> None:
        self.username = username
        self.last_logged = last_logged

    def validate(self) -> bool:
        return bool(re_username.search(self.username))
