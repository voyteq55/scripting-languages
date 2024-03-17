from lab_2_tools import get_std_input, print_filtered_rows

def print_requests_with_200_response(input):
    print_filtered_rows(input=input, predicate=has_response_code_200)

def has_response_code_200(fields):
    return fields['http_response'] == '200'

if __name__ == '__main__':
    print_requests_with_200_response(input=get_std_input())
