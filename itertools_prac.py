# itertools: products, permutations, combinations,
# accumulate, groupyby, and infinite iterator

#https://realpython.com/python-itertools/#what-is-itertools-and-why-should-you-use-it

from itertools import product

a = [1,2]
b = [3,4]

#create a cartesian product
prod = product(a,b)

print(list(prod))

from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))

#small permutaions with length of 2 
perm = permutations(a, 2)
print(list(perm))

from itertools import combinations, combinations_with_replacement
comb = combinations(a,2)
print(list(comb))

#when we need combination containing match of an element with tself as well.  (element,element)
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))


#accumulator is used for commulative calculations
from itertools import accumulate

#sum
a= [1,2,3,4]
acc = accumulate(a)
print(list(acc))

#max ele in list up until each index
a= [1,3,2,5,10,6,6]
max = accumulate(a, func=max)
print(list(max))

#itertools group by groups the elements together as
#per the key function

from itertools import groupby
def key_function(x):
    return x<5

group_obj = groupby(a, key=key_function)
for key, group in group_obj:
    print(key, list(group))

#complex use of groupby 

persons = [
    {"name":"John", "age": 20},
    {"name":"abc", "age":21},
    {"name":"cwa", "age":27},
    {"name":"jim", "age":22},
    {"name":"bob", "age":20},
    {"name":"john", "age":22},
]

#firt we will have to sort it by the key we want to use

persons.sort(key=lambda x: x['age'])
#group by age 
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))


#more itertools
from itertools import count, cycle, repeat

#count: creates infinite iterator
for i in count(10):
    print(i)
    if i == 100:
        break

#cycle: creates an infinite 
#iterator that keeps repeating elements
#of given lists for example fr belw list
# it will generate 1,2,3,1,2,3, 1,2,3 ...

a = [1,2,3]
count_val = 0
for i in cycle(a):
    print(i)
    if count_val == 13:
        break
    count_val += 1

#repeat: it will repeat given element infinitely

# for i in repeat(1):
#     print(i)