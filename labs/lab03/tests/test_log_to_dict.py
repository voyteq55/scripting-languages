from log_to_dict import log_to_dict
from datetime import datetime


def test_log_to_dict():
    log = [
        ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
        ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
        ('reddragon.ksc.nasa.gov', datetime(1995, 7, 10, 18, 2, 38), 'GET', '/htbin/cdt.pl', 500, 0),
        ('bos1e.delphi.com', datetime(1995, 7, 15, 11, 44, 33), 'GET', '/htbin/cdt_clock.pl', 200, 543)
    ]
    expected_dict = {
        '205.199.120.126': [
            {
                'host': '205.199.120.126',
                'time': datetime(1995, 7, 17, 17, 49, 33),
                'http_method': 'GET',
                'path': '/software/winvn/bluemarb.gif',
                'http_response': 200,
                'bytes_count': 4441
            }
        ],
        'bos1e.delphi.com': [
            {
                'host': 'bos1e.delphi.com',
                'time': datetime(1995, 7, 17, 18, 5, 57),
                'http_method': 'GET',
                'path': '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif',
                'http_response': 200,
                'bytes_count': 36998
            },
            {
                'host': 'bos1e.delphi.com',
                'time': datetime(1995, 7, 15, 11, 44, 33),
                'http_method': 'GET',
                'path': '/htbin/cdt_clock.pl',
                'http_response': 200,
                'bytes_count': 543
            }
        ],
        'reddragon.ksc.nasa.gov': [
            {
                'host': 'reddragon.ksc.nasa.gov',
                'time': datetime(1995, 7, 10, 18, 2, 38),
                'http_method': 'GET',
                'path': '/htbin/cdt.pl',
                'http_response': 500,
                'bytes_count': 0
            }
        ]
    }

    assert log_to_dict(log) == expected_dict