from datetime import date
from lab_2_tools import get_std_input, print_filtered_rows

month_name_to_number_dict = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
}

def print_requests_queried_on_friday(input):
    print_filtered_rows(input=input, predicate=is_on_friday)

def is_on_friday(fields):
    return get_date(fields["time"]).weekday() == 4

def get_date(time_field):
    day = int(time_field[0:2])
    month = month_name_to_number_dict[time_field[3:6]]
    year = int(time_field[7:11])
    return date(year, month, day)

if __name__ == '__main__':
    print_requests_queried_on_friday(input=get_std_input())
