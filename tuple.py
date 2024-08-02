# Tuple:collection data type ordered, immutable, allows dublicate elements
# used fr objects that bolong together
mytuple = ('Max', 28, 'Booston')

#single value in a () is not a tuple add a comma

#create a tuple from an iterable 
mytuple = tuple(['Max', 28, 'Booston'])

print(mytuple)

#access using index 
first_ele = mytuple[0]
print(first_ele)

#iteration
for i in mytuple:
    print(i)

#checking ele 
if 28 in mytuple:
    print("yes")

#len of elements in tuple
print(len(mytuple))

#count the occurence of soething in tuple 
print(mytuple.count(28))

#index of something 
print(mytuple.index(28))

#convert tuple to list 
myl = list(mytuple)
print(myl)

mytuple = list(myl)

#slicing 
mytuple2 = mytuple[1:3]
print(mytuple2)

#unpacking 
name, age, city = mytuple

print(name)
print(age)
print(city)

mytuple3 = (1,2,3,4,5,6)
i1, *i2, i3 = mytuple3

print(i1)
print(i3)
print(i2)

#tuple takes less mremry in comparison to
#list
import sys
myList = [1,2,3,4,5,6]
myTuple = (1,2,3,4,5,6)
print(sys.getsizeof(myList), 'bytes')
print(sys.getsizeof(myTuple), 'bytes')

#Working with tuples make the code mre efficient the lists
#according to the problem you are wrking on.


