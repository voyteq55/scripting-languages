from get_addrs import get_addrs
from datetime import datetime


def test_log_to_dict():
    log_dict = {
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
    expected_list = ['205.199.120.126', 'bos1e.delphi.com', 'reddragon.ksc.nasa.gov']

    assert get_addrs(log_dict) == expected_list