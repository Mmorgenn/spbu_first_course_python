import datetime
from functools import wraps
import inspect


def logger(log_file: str):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            function_arguments = inspect.signature(func).bind(*args, **kwargs).arguments
            formatted_arguments = (" ").join(
                f"{arg}={value}" for (arg, value) in function_arguments.items()
            )

            result_function = func(*args, **kwargs)

            with open(log_file, "a") as file_output:
                file_output.write(
                    f"{datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')} {func.__name__} {formatted_arguments} {result_function}\n"
                )

            return result_function

        return inner

    return decorator
