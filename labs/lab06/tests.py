import pytest
from sshlogentry import SSHLogEntry
from specialized_ssh_log_entries import FailedPassSSHLogEntry, AcceptedPassSSHLogEntry, ErrorSSHLogEntry, OtherSSHLogEntry
from ipaddress import IPv4Address


@pytest.mark.parametrize(
    "line, ipv4",
    [
        (
            "Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]",
            IPv4Address("212.47.254.145")
        )
    ]
)
def test_ssh_log_entry_ipv4(line: str, ipv4: IPv4Address):
    assert OtherSSHLogEntry(line).ipv4() == ipv4


def test_ssh_log_entry_derived_classes():
    failed_pass_etnry = FailedPassSSHLogEntry("Dec 10 11:04:41 LabSZ sshd[25537]: Failed password for root from 183.62.140.253 port 36027 ssh2")
    assert failed_pass_etnry.port == 36027
    assert failed_pass_etnry.failed_user == "root"
    assert failed_pass_etnry.validate()

    accepted_pass_entry = AcceptedPassSSHLogEntry("Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2")
    assert accepted_pass_entry.port == 49116
    assert accepted_pass_entry.accepted_user == "fztu"
    assert accepted_pass_entry.validate()

    error_entry = ErrorSSHLogEntry("Dec 10 11:03:40 LabSZ sshd[25448]: error: Received disconnect from 103.99.0.122: 14: No more user authentication methods available. [preauth]")
    assert error_entry.error_type == "14: No more user authentication methods available. [preauth]"
    assert error_entry.validate()

    other_entry = OtherSSHLogEntry("Dec 10 06:55:46 LabSZ sshd[24200]: reverse mapping checking getaddrinfo for ns.marryaldkfaczcz.com [173.234.31.186] failed - POSSIBLE BREAK-IN ATTEMPT!")
    assert other_entry.validate()


@pytest.mark.parametrize(
    "ssh_entry, has_ip",
    [
        (
            OtherSSHLogEntry("Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]"),
            True
        ),
        (
            OtherSSHLogEntry("Dec 10 07:11:42 LabSZ sshd[24224]: pam_unix(sshd:auth): check pass; user unknown"),
            False
        ),
        (
            FailedPassSSHLogEntry("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"),
            True
        )
    ]
)
def test_has_ip(ssh_entry: SSHLogEntry, has_ip: bool):
    assert ssh_entry.has_ip == has_ip


@pytest.mark.parametrize(
    "entry1, entry2, expected_result",
    [
        (
            ErrorSSHLogEntry("Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]"),
            ErrorSSHLogEntry("Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]"),
            True
        ),
        (
            ErrorSSHLogEntry("Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]"),
            OtherSSHLogEntry("Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]"),
            False
        ),
        (
            ErrorSSHLogEntry("Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]"),
            ErrorSSHLogEntry("Dec 10 07:11:42 LabSZ sshd[24224]: pam_unix(sshd:auth): check pass; user unknown"),
            False
        ),
        (
            ErrorSSHLogEntry("Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]"),
            None,
            False
        )
    ]
)
def test_entries_equality(entry1: SSHLogEntry, entry2: SSHLogEntry, expected_result: bool):
    assert (entry1 == entry2) == expected_result


@pytest.mark.parametrize(
    "smaller_entry, greater_entry",
    [
        (
            FailedPassSSHLogEntry("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"),
            OtherSSHLogEntry("Dec 10 07:02:47 LabSZ sshd[24203]: Connection closed by 212.47.254.145 [preauth]"),
        ),
        (
            OtherSSHLogEntry("Dec 10 06:55:46 LabSZ sshd[24200]: reverse mapping checking getaddrinfo for ns.marryaldkfaczcz.com [173.234.31.186] failed - POSSIBLE BREAK-IN ATTEMPT!"),
            OtherSSHLogEntry("Dec 10 07:11:42 LabSZ sshd[24224]: pam_unix(sshd:auth): check pass; user unknown")
        )
    ]
)
def test_entries_inequality(smaller_entry: SSHLogEntry, greater_entry: SSHLogEntry):
    assert smaller_entry < greater_entry
    assert not greater_entry < smaller_entry
    assert greater_entry > smaller_entry
    assert not smaller_entry > greater_entry


@pytest.mark.parametrize(
    "entry1, other",
    [
        (
            FailedPassSSHLogEntry("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"),
            None
        ),
        (
            OtherSSHLogEntry("Dec 10 06:55:46 LabSZ sshd[24200]: reverse mapping checking getaddrinfo for ns.marryaldkfaczcz.com [173.234.31.186] failed - POSSIBLE BREAK-IN ATTEMPT!"),
            25
        )
    ]
)
def test_entries_lt_error(entry1: SSHLogEntry, other: object):
    with pytest.raises(TypeError):
        entry1 < other


@pytest.mark.parametrize(
    "entry1, other",
    [
        (
            FailedPassSSHLogEntry("Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"),
            None
        ),
        (
            OtherSSHLogEntry("Dec 10 06:55:46 LabSZ sshd[24200]: reverse mapping checking getaddrinfo for ns.marryaldkfaczcz.com [173.234.31.186] failed - POSSIBLE BREAK-IN ATTEMPT!"),
            25
        )
    ]
)
def test_entries_gt_error(entry1: SSHLogEntry, other: object):
    with pytest.raises(TypeError):
        entry1 > other