
"""
Context managers are useful for managing resources.
The begin with a "with" statement
"""

"""
Creating custom context managers
"""

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')

with ManagedFile('notes.txt') as file:
    print("do something here")
    file.write("some too..")
