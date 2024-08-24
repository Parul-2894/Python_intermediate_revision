import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #Do ..
        result = func(*args, **kwargs)
        #Do..
        return result

    return wrapper


@my_decorator
def my_funcion(args):
    #Do ...
    return result

