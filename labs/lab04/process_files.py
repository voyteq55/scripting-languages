import os, sys, json
from subprocess import Popen, PIPE
from collections import defaultdict


def get_process_outputs(filenames):
    process = Popen(["python", "analyze_file.py"], stdin=PIPE, stdout=PIPE)
    for filename in filenames:
        path = os.path.join(dir_path, filename)
        process.stdin.write(f'{path}\n'.encode(encoding="utf-8"))
    process.stdin.close()
    return [line.decode(encoding="utf-8").rstrip() for line in process.stdout.readlines()]


def get_stats(output_dicts):
    current_file_count = len(output_dicts)
    char_count_sum = sum(output_dict["char_count"] for output_dict in output_dicts)
    word_count_sum = sum(output_dict["word_count"] for output_dict in output_dicts)
    row_count_sum = sum(output_dict["row_count"] for output_dict in output_dicts)

    words_counts = defaultdict(int)
    chars_counts = defaultdict(int)
    for output_dict in output_dicts:
        words_counts[output_dict["most_frequent_word"]] += 1
        chars_counts[output_dict["most_frequent_char"]] += 1
    most_frequent_word = max(words_counts, key=lambda word: words_counts[word])
    most_frequent_char = max(chars_counts, key=lambda char: chars_counts[char])

    return {
        "file_count": current_file_count,
        "char_count_sum": char_count_sum,
        "word_count_sum": word_count_sum,
        "row_count_sum": row_count_sum,
        "most_frequent_word": most_frequent_word,
        "most_frequent_char": most_frequent_char
    }


if __name__ == "__main__":
    try:
        dir_path = sys.argv[1]
        filenames = os.listdir(dir_path)
        output_lines = get_process_outputs(filenames)
        stats = get_stats([json.loads(line) for line in output_lines])
        print(json.dumps(stats))
        
    except IndexError:
        print("No directory path provided", file=sys.stderr)
        exit(1)
    except FileNotFoundError:
        print("Directory not found", file=sys.stderr)
        exit(1)