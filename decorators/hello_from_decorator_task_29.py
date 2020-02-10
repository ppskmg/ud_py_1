from functools import wraps


def hello_from_decorator(func):
    """
    Decoration function
    if args and kwargs empty return EMPTY, add string in result "Hello from decorator"
    :param func:
    :return: string, func args and kwargs
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func()
        key_word_arguments = []
        for key, value in kwargs.items():
            key_word_arguments.append(key.upper() + ':' + "'" + value + "'")

        kws = 'EMPTY' if kwargs == {} else ', '.join(key_word_arguments)
        arguments = 'EMPTY' if args == () else ', '.join(args).upper()

        return str(result) + f' => args: {arguments} => kwargs: {kws} => add string: Hello from decorator!'
    return wrapper


@hello_from_decorator
def my_function():
    return 'Function return string and: '


print(my_function('arg_1', 'arg_2', 'arg3', modul='functools', func_in_modul='wraps'))
# print(my_function.__name__)
# print(hello_from_decorator.__doc__)