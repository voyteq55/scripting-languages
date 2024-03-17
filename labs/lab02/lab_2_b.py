from lab_2_tools import get_parsed_dict, get_std_input, get_bytes_count

def print_data_size_in_gb(input):
    current_bytes_count = 0
    for line in input:
        fields = get_parsed_dict(line.rstrip())
        current_bytes_count += get_bytes_count(fields["bytes_count"])
    gigabytes_count = current_bytes_count // (10 ** 9)
    print(gigabytes_count)

if __name__ == '__main__':
    print_data_size_in_gb(input=get_std_input())
