from lab_2_tools import get_parsed_dict, get_std_input, get_bytes_count

def print_largest_resource(input):
    current_largest_resource_size = 0
    current_largest_resource_path = ""
    for line in input:
        fields = get_parsed_dict(line.rstrip())
        current_size = get_bytes_count(fields['bytes_count'])
        if current_size > current_largest_resource_size:
            current_largest_resource_path = fields['path']
            current_largest_resource_size = current_size
    print(current_largest_resource_path, current_largest_resource_size)

if __name__ == '__main__':
    print_largest_resource(input=get_std_input())