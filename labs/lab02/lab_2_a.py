from lab_2_tools import get_parsed_dict

def print_code_count(input, code):
    current_code_count = 0
    for line in input:
        fields = get_parsed_dict(line.rstrip())
        if fields['http_response'] == code:
            current_code_count += 1
    print(current_code_count)
