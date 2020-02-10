from functools import wraps


def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            raise ValueError('Function must have less than 3 arguments!')
        return func(*args, **kwargs)
    return wrapper


@prohibit_more_than_2_args
def my_func(*args):
    return args


print(my_func('args_1', 'args_2', 'this_value_error'))