#Sets: unordered, mutable and no duplicates

myset = set("Hello")
print(myset)

myset2 = {1,2}

print(type(myset2))

#add eles
myset2.add(1)
myset2.add(2)

#remove eles
# print(myset2)
# myset2.remove(2)
# print(myset2)

#clear to empty set
# myset2.clear()
# print(myset2)

#iteration
for i in myset2:
    print(i)

if 1 in myset2:
    print("yes")

#union
oddnum = {1,3,5,7,9}
evens = {0,2,4,6,8}
prime = {2,3,5,7}

uoe = oddnum.union(evens)
print(uoe)
inter_uoe_prime = uoe.intersection(prime)
print(inter_uoe_prime)

#check subsets 
print(prime.issubset(oddnum))

#check if two sets have all differenct elements
print(oddnum.isdisjoint(evens))

#copy 
#no simple assignement should be used because
#both the copies point to the same thing.
odd_copy = oddnum.copy()
print(oddnum)
odd_copy.add(11)
print(odd_copy)


# frozen set is a st but immutable
a = frozenset([1,2,3,4,5])





