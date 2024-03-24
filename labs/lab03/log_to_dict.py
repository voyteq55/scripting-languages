from entry_to_dict import entry_to_dict

def log_to_dict(log):
    current_dict = {}
    for entry in log:
        host = entry[0]
        if host not in current_dict:
            current_dict[host] = []
        current_dict[host].append(entry_to_dict(entry))
    return current_dict
