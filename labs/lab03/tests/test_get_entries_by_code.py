import pytest
from datetime import datetime
from get_entries_by_code import get_entries_by_code

@pytest.mark.parametrize('log, code, filtered_log', [
    (
        [
            ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
            ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0),
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998)
        ],
        200,
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
        300,
        []
     ),
     (
        [
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0),
            ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
        ],
        404,
        [
            ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0)
        ]
     ),
     (
         [
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441)
         ],
         12345,
         None
     )
])
def test_get_entries_by_code(log, code, filtered_log):
    assert get_entries_by_code(log, code) == filtered_log