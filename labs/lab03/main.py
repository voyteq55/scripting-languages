from read_log import read_log
from get_entries_by_extension import get_entries_by_extension
from print_entries import print_entries
from log_to_dict import log_to_dict
from print_dict_entry_dates import print_dict_entry_dates

def main():
    print_entries(get_entries_by_extension(read_log(), '.jpg'))
    # print_dict_entry_dates(log_to_dict(read_log()))

if __name__ == '__main__':
    main()
