import os, sys, json
from collections import defaultdict


def get_file_stats(filepath):
    path = os.path.abspath(filepath)
    with open(filepath) as file:
        char_count = 0
        word_count = 0
        row_count = 0
        words_counts = defaultdict(int)
        chars_counts = defaultdict(int)
        for line in file.readlines():
            char_count += len(line)
            row_count += 1
            for char in line:
                chars_counts[char] += 1
            for word in line.split():
                words_counts[word] += 1
                word_count += 1
    most_frequent_word = max(words_counts, key=lambda word: words_counts[word])
    most_frequent_char = max(chars_counts, key=lambda char: chars_counts[char])

    return {
        "path": path,
        "char_count": char_count,
        "word_count": word_count,
        "row_count": row_count,
        "most_frequent_word": most_frequent_word,
        "most_frequent_char": most_frequent_char
    }


if __name__ == "__main__":
    for filepath in sys.stdin:
        print(json.dumps(get_file_stats(filepath.rstrip())))
