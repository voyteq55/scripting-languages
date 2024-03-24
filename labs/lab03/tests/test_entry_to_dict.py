from entry_to_dict import entry_to_dict
from datetime import datetime
import pytest


def test_entry_to_dict():
    entry = ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
    expected_dict = {
        'host': '205.199.120.126',
        'time': datetime(1995, 7, 17, 17, 49, 33),
        'http_method': 'GET',
        'path': '/software/winvn/bluemarb.gif',
        'http_response': 200,
        'bytes_count': 4441
    }
    assert entry_to_dict(entry) == expected_dict
