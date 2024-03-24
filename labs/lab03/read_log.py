import sys, re
from datetime import datetime

def read_log():
    return get_log(sys.stdin)

def get_log(input):
    return [entry for line in input if (entry := get_entry(line.rstrip())) is not None]
    
def get_entry(line):
    fields = re.split('\]?\"? \"?\[?', line)
    datetime_format = '%d/%b/%Y:%H:%M:%S'
    try:
        host = fields[0]
        time = datetime.strptime(fields[3], datetime_format)
        http_method = fields[5]
        path = fields[6]
        http_response = int(fields[-2])
        bytes_count = int(bytes) if (bytes := fields[-1]).isdigit() else 0
        return host, time, http_method, path, http_response, bytes_count
    except (IndexError, ValueError):
        return None
