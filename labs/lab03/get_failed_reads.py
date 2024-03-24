def get_failed_reads(log, should_return_one_list=False):
    entries_with_4xx_code = []
    entries_with_5xx_code = []
    for entry in log:
        if 400 <= (http_response := entry[4]) <= 499:
            entries_with_4xx_code.append(entry)
        elif 500 <= http_response <= 599:
            entries_with_5xx_code.append(entry)
    return entries_with_4xx_code + entries_with_5xx_code if should_return_one_list else (entries_with_4xx_code, entries_with_5xx_code)
