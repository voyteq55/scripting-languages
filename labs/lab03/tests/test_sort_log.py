import pytest
import datetime
from sort_log import sort_log

@pytest.mark.parametrize('log, sort_index, expected_sorted_log', [
    (
        [
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
            ('bos1e.delphi.com', datetime.datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998)
        ],
        0,
        [
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
            ('bos1e.delphi.com', datetime.datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998)
        ]
     ),
     (
        [
            ('bos1e.delphi.com', datetime.datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
        ],
        1,
        [
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
            ('bos1e.delphi.com', datetime.datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998)
        ]
     ),
     (
         [
            ('bos1e.delphi.com', datetime.datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
         ],
         10,
         [
            ('bos1e.delphi.com', datetime.datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('205.199.120.126', datetime.datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
         ]
     )
])
def test_sort_log(log, sort_index, expected_sorted_log):
    assert sort_log(log, sort_index) == expected_sorted_log