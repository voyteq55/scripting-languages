def entry_to_dict(entry):
    dict_keys = ['host', 'time', 'http_method', 'path', 'http_response', 'bytes_count']
    return {key: entry[index] for index, key in enumerate(dict_keys)}