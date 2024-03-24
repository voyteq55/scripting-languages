import pytest
import datetime
from get_entries_by_addr import get_entries_by_addr

@pytest.mark.parametrize('log, host_address, filtered_log', [
    (
        [
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
            ('bos1e.delphi.com', datetime.datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998)
        ],
        '205.199.120.126',
        [
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
        ]
     ),
     (
        [
            ('bos1e.delphi.com', datetime.datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
        ],
        '',
        []
     ),
     (
         [
            ('bos1e.delphi.com', datetime.datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
         ],
         '205.199.120.126',
         [
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
         ]
     )
])
def test_get_entries_by_addr(log, host_address, filtered_log):
    assert get_entries_by_addr(log, host_address) == filtered_log