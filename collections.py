# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

#counter counts the occurence and prepares a dictnary
str = "aaaaabbbbccc"
my_counter = Counter(str)
print(my_counter)

mylst = ['abc', 'abc', 'bcd']
my_counter = Counter(mylst)
print(my_counter)

#print most common value using counter
print(my_counter.most_common(1)[0][0])

#namedtuple
from collections import namedtuple

"""
In Python, NamedTuple is present inside the collections module. 
It provides a way to create simple, lightweight data structures similar to a class, but without the overhead of defining a full class. 
Like dictionaries, they contain keys that are hashed to a particular value. 
On the contrary, it supports both access from key-value and iteration, 
the functionality that dictionaries lack.
"""
Point = namedtuple('Point', ['x','y'])
pt = Point(1, -4)
print(pt)

pt2 = Point(2,6)
print(pt2.x)
print(pt2[0])

from collections import defaultdict
#it will have a default value if the key is not 
#set yet
#so if you access a key, it will return a 
#default value of type you mention in the brackets

d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d['c'])


from collections import deque
# is a double ended queue and add and 
#remove eles from both ends

d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

# we can clear the deque 
# d.clear()
# print(d)

#we extend deque  using extend
d.extend([1,2,3])
print(d)

#we can rotate as well
d.rotate(1)
print(d)