
"""
With *args yu can pass any number of arguments. 
With kwargs yu can pass any number of positional arguments
"""
def foo(a,b, *args, **kwargs):
    print(a,b)

    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1,2,3,4,5,six=6,seven=7)