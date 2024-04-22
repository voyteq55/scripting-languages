import os, sys, re

DEFAULT_LINES_COUNT = 10


def tail(input_stream, lines_count):
    current_index = 0
    current_tail = [None] * lines_count
    for line in input_stream:
        current_tail[current_index] = line.rstrip()
        current_index = (current_index + 1) % lines_count
    return [line for real_index in range(lines_count) if (line := current_tail[(current_index + real_index) % lines_count])]


def parse_args(args):
    regex_pattern = r'--lines=(\d+)'
    if not args:
        return {}
    if len(args) == 1:
        if regex_match := re.match(pattern=regex_pattern, string=args[0]):
            return {"lines_count": int(regex_match.group(1))}
        return {"filepath": args[0]}
    if len(args) > 2:
        raise ValueError("Illegal number of arguments")
    if regex_match := re.match(pattern=regex_pattern, string=args[0]):
        return {"filepath": args[1], "lines_count": int(regex_match.group(1))}
    if regex_match := re.match(pattern=regex_pattern, string=args[1]):
        return {"filepath": args[0], "lines_count": int(regex_match.group(1))}
    raise ValueError("Illegal arguments")


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
        lines_count = args.get("lines_count", DEFAULT_LINES_COUNT)
        if filepath := args.get("filepath"):
            with open(filepath) as file:
                for line in tail(file, lines_count):
                    print(line)
        else:
            for line in tail(sys.stdin, lines_count):
                print(line)
    except (ValueError, FileNotFoundError) as error:
        print(error, file=sys.stderr)
        exit(1)
