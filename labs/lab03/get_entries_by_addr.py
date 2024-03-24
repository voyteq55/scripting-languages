def get_entries_by_addr(log, host_address):
    return [entry for entry in log if entry[0] == host_address]
