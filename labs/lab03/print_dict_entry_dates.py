def print_dict_entry_dates(log_dict):
    for host in log_dict:
        requests_count, first_request_time, last_request_time, percentage_of_code_200_to_all = get_host_info(log_dict[host])
        print(f'address: {host}\nnumber of requests: {requests_count}')
        print(f'first request: {first_request_time}')
        print(f'last request: {last_request_time}')
        print(f'{percentage_of_code_200_to_all:.2f}% with code 200\n')

def get_host_info(entries):
    requests_count = len(entries)
    first_request_time = min(entries, key=lambda entry: entry['time'])['time']
    last_request_time = max(entries, key=lambda entry: entry['time'])['time']
    requests_with_code_200_count = sum(1 for entry in entries if entry['http_response'] == 200)
    percentage_of_code_200_to_all = 100 * requests_with_code_200_count / requests_count
    return requests_count, first_request_time, last_request_time, percentage_of_code_200_to_all