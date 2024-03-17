import re
from lab_2_tools import get_parsed_dict, get_std_input

def print_graphics_to_other_resources_ratio(input):
    current_graphics_files_count = 0
    current_other_resources_count = 0
    for line in input:
        fields = get_parsed_dict(line.rstrip())
        if is_graphics_file(filepath=fields['path']):
            current_graphics_files_count += 1
        else:
            current_other_resources_count += 1
    print(current_graphics_files_count / current_other_resources_count)

def is_graphics_file(filepath):
    graphics_pattern = '\.gif$|\.jpg$|\.jpeg$|\.xbm$'
    return bool(re.search(pattern=graphics_pattern, string=filepath))

if __name__ == '__main__':
    print_graphics_to_other_resources_ratio(input=get_std_input())
