from read_log import get_entry, get_log
from datetime import datetime
import pytest


@pytest.mark.parametrize('line, expected_entry', [
    (
        '205.199.120.126 - - [17/Jul/1995:17:49:33 -0400] "GET /software/winvn/bluemarb.gif HTTP/1.0" 200 4441',
        ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
    ),
    (
        'bos1e.delphi.com - - [17/Jul/1995:18:05:57 -0400] "GET /shuttle/missions/sts-70/images/KSC-95EC-0540.gif" 200 36998',
        ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998)
    ),
    (
        'www-b1.proxy.aol.com - - [10/Jul/1995:10:44:39 -0400] "GET /history/apollo/apollo-13/apollo-13.htm/ HTTP/1.0" 404 -',
        ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0)
    ),
    (
        'abcdef',
        None
    ),
    (
        '',
        None
    )
])
def test_get_entry(line, expected_entry):
    assert get_entry(line) == expected_entry


def test_get_log():
    input = [
        '205.199.120.126 - - [17/Jul/1995:17:49:33 -0400] "GET /software/winvn/bluemarb.gif HTTP/1.0" 200 4441',
        'abcdef',
        'bos1e.delphi.com - - [17/Jul/1995:18:05:57 -0400] "GET /shuttle/missions/sts-70/images/KSC-95EC-0540.gif" 200 36998',
        ''
    ]
    expected_entries = [
        ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
        ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998)
    ]
    assert get_log(input) == expected_entries
