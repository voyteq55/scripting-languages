def get_entries_by_code(log, code):
    if code < 100 or code > 599:
        return None
    return [entry for entry in log if entry[4] == code]