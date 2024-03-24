from get_failed_reads import get_failed_reads
from datetime import datetime
import pytest

@pytest.mark.parametrize('log, should_return_one_list, filtered_log', [
    (
        [
            ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
            ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0),
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('reddragon.ksc.nasa.gov', datetime(1995, 7, 10, 18, 2, 38), 'GET', '/htbin/cdt.pl', 500, 0)
        ],
        True,
        [
            ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0),
            ('reddragon.ksc.nasa.gov', datetime(1995, 7, 10, 18, 2, 38), 'GET', '/htbin/cdt.pl', 500, 0)
        ]
     ),
     (
         [
            ('205.199.120.126', datetime(1995, 7, 17, 17, 49, 33), 'GET', '/software/winvn/bluemarb.gif', 200, 4441),
            ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0),
            ('bos1e.delphi.com', datetime(1995, 7, 17, 18, 5, 57), 'GET', '/shuttle/missions/sts-70/images/KSC-95EC-0540.gif', 200, 36998),
            ('reddragon.ksc.nasa.gov', datetime(1995, 7, 10, 18, 2, 38), 'GET', '/htbin/cdt.pl', 500, 0)
        ],
        False,
        (
            [
                ('www-b1.proxy.aol.com', datetime(1995, 7, 10, 10, 44, 39), 'GET', '/history/apollo/apollo-13/apollo-13.htm/', 404, 0)
            ],
            [
                ('reddragon.ksc.nasa.gov', datetime(1995, 7, 10, 18, 2, 38), 'GET', '/htbin/cdt.pl', 500, 0)
            ]
        )
     )
])
def test_get_failed_reads(log, should_return_one_list, filtered_log):
    assert get_failed_reads(log, should_return_one_list) == filtered_log