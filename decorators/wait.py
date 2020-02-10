from time import sleep
from functools import wraps

#Интересное поведение, запускается при указании декоратора без вызова функции, если не указать вложенную функцию

def wait(n):
    """
    Decorator function
    :param n: int sec
    :return: counting every second and return string finished
    """
    def wrapper(func):
        print(f'Delay {n} sec \n')
        for i in range(1, n):
            print(str(i) + ' sec')
            sleep(i)
        print(f'There was a pause {n} seconds before execution {func.__name__} \n')
        return func
    return wrapper


def wait_2(n):
    def wrapper(func):
        sleep(n)
        print(f'There was a pause {n} seconds before execution {func.__name__} \n')
        return func
    return wrapper


# РЕШЕНИЕ
def wait_3(n):
    """
    Decorator timer function
    :param n: int sec
    :return: counting every second and return string finished (countdown)
    """
    def inner_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            i = n + 1
            while i > 1:
                i -= 1
                print(str(i) + ' sec' )
                sleep(i)
            print(f'There was a pause {n} seconds before execution {func.__name__} \n')
            return func(*args, **kwargs)
        return wrapper

    return inner_func



@wait(3)
def my_func():
    print('finished')



#@wait_2(3)
def my_func_2():
    print('finished')


@wait_3(3)
def my_func_3():
    print('finished')


# my_func()
# my_func_2()
my_func_3()