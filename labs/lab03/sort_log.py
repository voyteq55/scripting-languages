import sys

def sort_log(log, sort_index=0):
    try:
        return sorted(log, key=lambda entry: entry[sort_index])
    except IndexError:
        print(f'invalid sort index out of bounds: {sort_index}', file=sys.stderr)
        return log
