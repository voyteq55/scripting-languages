from lab_2_tools import get_std_input, print_filtered_rows

def print_requests_from_between_22_and_6(input):
    print_filtered_rows(input=input, predicate=is_from_between_22_and_6)

def is_from_between_22_and_6(fields):
    hour = get_hour(fields['time'])
    return hour >= 22 or hour < 6

def get_hour(time_field):
    return int(time_field[12:14])

if __name__ == '__main__':
    print_requests_from_between_22_and_6(input=get_std_input())
