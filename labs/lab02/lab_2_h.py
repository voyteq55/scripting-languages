from lab_2_tools import get_std_input, print_filtered_rows

def print_requests_from_poland(input):
    print_filtered_rows(input=input, predicate=is_from_poland)

def is_from_poland(fields):
    return fields['host'][-3:] == '.pl'

if __name__ == '__main__':
    print_requests_from_poland(input=get_std_input())
