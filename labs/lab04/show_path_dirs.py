import os, sys

PATH = "PATH"
SHOW_CONTENTS_FLAG = "--show-contents"

def get_path_dirs():
    return os.environ.get(PATH).split(os.pathsep)

def get_path_dirs_with_contents(dirs):
    for dir_path in dirs:
        try:
            dir_contents = os.listdir(path=dir_path)
        except FileNotFoundError:
            dir_contents = []
        yield f"{dir_path}: {dir_contents}"

if __name__ == "__main__":
    path_dir_lines = get_path_dirs()
    if len(sys.argv) >= 2 and sys.argv[1] == SHOW_CONTENTS_FLAG:
        path_dir_lines = get_path_dirs_with_contents(path_dir_lines)
    for line in path_dir_lines:
        print(line)
