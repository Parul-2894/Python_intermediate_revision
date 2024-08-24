"""
    Generators are functions that return an object that can be iterator over. 
    They generate items one at a time and only when you ask for it.
    They generate the items insde the object lazily, becasue of this they are much more memory efficient.
    than other sequence objects when you have to deal with large datasets.
    They are a powerful advanced python technique.
    A generator is defined like a normal function but instead of a yeild keywrd we use 
    a return keyword. 

    
"""

def myGenerator():
    yield 1
    yield 2
    yield 3

g = myGenerator() # this create a genertor object.
# now  can lop over this generator object

# for i in g:
#     print(i)

# I can also get values one at a time using next()
# It goes up until tthe first yeild statment returns it and
# pauses there
# Then when call the next() function second time, it check from the
# previous yeild onwards. 
#when there it nothng to yeild anymore, it throws an exception "StopIterations".
#Next remembers the state.

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)


"""
Advantages of Generators
1. They are very memory efficient.
"""

#Exmaple of a simple function to return a list of 
#first n numbers and find their sum

def firstn(n):
    num_list = []
    num = 0
    while num<n:
        num_list.append(num)
        num += 1
    return num_list

print(sum(firstn(10)))

#same abve function using generator

def firstn_generatr(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generatr(10)))

#so by using generators we do not need to use a list to store the values.


"""
Example :
Creating Fibnacci series using yeild 
"""

def fibonacci(limit):
    # 0 1 1 2 3 5 8

    a,b = 0,1 
    while a < limit:
        yield a 
        a,b = b, b+a
        
fib_gen = fibonacci(10)

for i in fib_gen:
    print(i)


#Generator Sequence 
myGenerator = (i for i in range(10) if i%2 == 0)
 
#generator exp
print("Gen exp")
print(next(myGenerator))

# it is similar to list comprehension just [] is replace by ()

#yu can convert a generator to a list using
#list()
print(list(myGenerator))