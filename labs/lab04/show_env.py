import sys, os

def get_filtered_env_var_keys(*args):
    if args:
        allowed_keys = set(args)
        predicate = lambda key: key in allowed_keys
    else:
        predicate = lambda key: True

    return filter(predicate, os.environ)

def get_env_var_keys_from_cli():
    return get_filtered_env_var_keys(*sys.argv[1:])

if __name__ == "__main__":
    for key in sorted(get_env_var_keys_from_cli()):
        print(f"{key}: {os.environ.get(key)}")
