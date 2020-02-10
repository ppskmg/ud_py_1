from functools import wraps


def print_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)
        func()
        # return func
    return wrapper


@print_args
def some_func():
    print('Some code')
#
#
# # some_func('arara','adsa')
# # print(some_func.__name__)
some_func('arara')
