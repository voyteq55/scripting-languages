import logging_setup
import logging, time
from datetime import datetime


def log(log_level: str):
    logging_setup.logger.setLevel(log_level)
    logging_setup.stream_handler.setLevel(log_level)

    def decorator(obj):
        if isinstance(obj, type):
            class Wrapper_class(obj):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    logging.info(f"initializing instance of class {obj.__name__}")
            return Wrapper_class

        def function_wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = obj(*args, **kwargs)
            end = time.perf_counter()
            logging.info(f"{datetime.now()} executing function {obj.__name__} with args: {args}, kwargs: {kwargs}, returns {result} (execution time: {end - start:.8f} s)")
            return result
        return function_wrapper 
    return decorator
