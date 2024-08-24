"""
In place of a function decorator you can also use a
function decorators/ 
"""

"""
Here in the example we will check how many times we called a function
"""

from typing import Any


class CountCalls():
    def __init__(self, func):
        self.func = func
        self.numCalls = 0

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.numCalls += 1
        self.func(*args, **kwds)
        print(f'This is executed {self.numCalls} times')



@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()
say_hello()

