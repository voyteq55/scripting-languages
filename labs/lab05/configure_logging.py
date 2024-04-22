import logging, sys

def configure():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_formatter = logging.Formatter('stdout: %(levelname)s: %(message)s')
    stdout_handler.setFormatter(stdout_formatter)

    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)
    stderr_formatter = logging.Formatter('stderr: %(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stderr_handler.setFormatter(stderr_formatter)

    logger.addHandler(stdout_handler)
    logger.addHandler(stderr_handler)


configure()