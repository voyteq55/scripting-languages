def get_entries_by_extension(log, extension):
    if not extension:
        return None
    return [entry for entry in log if (ext_length := len(extension)) <= len(path := entry[3]) and path[-ext_length:] == extension]
