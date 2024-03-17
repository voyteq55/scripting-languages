import re
import sys

def get_parsed_dict(line):
    fields = re.split('\]?\"? \"?\[?', line)
    field_dict = {}
    try:
        field_dict['host'] = fields[0]
        field_dict['time'] = fields[3]
        field_dict['http_method'] = fields[5]
        field_dict['path'] = fields[6]
        field_dict['http_response'] = fields[-2]
        field_dict['bytes_count'] = fields[-1]
    except IndexError:
        print(f'Error processing line:\n{line}', file=sys.stderr)
    return field_dict

def get_std_input():
    return sys.stdin

def get_bytes_count(bytes_count_field):
    if bytes_count_field == '-':
        return 0
    return int(bytes_count_field)

def print_filtered_rows(input, predicate):
    for line in input:
        fields = get_parsed_dict(line.rstrip())
        if predicate(fields):
            print(line.rstrip())
