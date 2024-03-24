from get_entries_by_extension import get_entries_by_extension
from datetime import datetime
import pytest

@pytest.mark.parametrize('log, extension, filtered_log', [
    (
        [
            ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
            ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0),
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998)
        ],
        "gif",
        [
            ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998)
        ]
     ),
     (
        [
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0),
            ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
        ],
        'html',
        []
     ),
     (
        [
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0),
            ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
        ],
        "shuttle/missions/sts-70/images/KSC-95EC-0540.gif",
        [
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998)
        ]
     ),
     (
        [
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0),
            ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
        ],
        '',
        None
     )
])
def test_get_entries_by_extension(log, extension, filtered_log):
    assert get_entries_by_extension(log, extension) == filtered_log