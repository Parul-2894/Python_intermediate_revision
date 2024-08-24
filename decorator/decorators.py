"""
Decorators allow you to add new functionality to an existing function

Functions are first class objects that means they can be defined in a function
can be passed as an argument and returned as well. 

"""

def start_end_decorator(func):

    def wrapper():
        print('start')
        func()
        print('stop')

    return wrapper

@start_end_decorator
def print_name():
    print('alex')

print_name()

#what happens if our function takes some args

def add(func):

    def wrapper(*args, **kwargs):
        print("addition", args[0])
        result = func(*args, **kwargs)
        print("Done")
        return result

    return wrapper


@add
def add5(x):
    return x + 5

print(add5(10))


"""
when a function is wrapped inside another function
python assumes its identity to be wrapper.
In order to ensure the the wapped function doesn't lose
ts identity. we can use functool.wraps function
"""

import functools
def add(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("addition", args[0])
        result = func(*args, **kwargs)
        print("Done")
        return result

    return wrapper


@add
def add5(x):
    return x + 5

print(help(add5))
print(add5.__name__)