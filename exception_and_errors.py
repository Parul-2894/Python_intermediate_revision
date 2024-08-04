# Errors and Exceptions 

#Syntax : Errors when parser detects a syntactically incorrect error
#Exception : Error when a statement is syntactiaclly correct

#exception example 

#Type error
# a = 5+'10'

# #module not found 
# import somemod

# #NameError if variable not defined
# a=5
# b = c

# #FileNotFound
# f=open('somefile.txt') 

#if you want an exception to occur
#we can use raise

x = -5
# if x<0:
    # raise Exception('x should be greate than 0')

# you can als use assert 
#assert(condition), 'any message on error'
# assert(x>=0), 'x is not positive'

try:
    a= 5/0
except Exception as e:
    print(e)
finally:
    print('runs always')

# Create you own errors:

class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message  = message
        self.value = value

def test_value(x):
    if x> 100:
        raise ValueTooHighError('value is to high')
    if x<5:
        raise ValueTooLowError('value is too low', x)
    

try:  
    test_value(101)
except Exception as e:
    print(e)


try:  
    test_value(1)
except Exception as e:
    print(e.message, e.value)
   