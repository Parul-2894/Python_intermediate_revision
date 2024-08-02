#Lists : ordered, mutable, alloows duplicate elements

#creation 
myList = ["banana", "cherry", "apple"]

#Iterations
for i in myList:
    print(i)

#how many eles:
print(len(myList))

#append
myList.append("orange")
print(myList)

#insert at spec location
#insert(index, value)
myList.insert(1, "blueberry")
print(myList)

#remove Items
#pop : last item removed
myList.pop()
print(myList)

#remove specific item
#remove : remove an item by value 
myList.remove("banana")
print(myList)

#empty list
# myList.clear()
# print(myList)

#reverse list
myList.reverse()

print(myList)

#sort list changes original list
# myList.sort()
# print(myList)

# if you don't want too change original list use
#sorted
new_list = sorted(myList)
print(new_list)
print(myList)

#repeat element multiple times
myList = [1,2,3,4,5]
print(myList)

#plus operator
myList2 = [1,2,3,4,5]
new_list = myList2 + myList
print(new_list)

#slicing
slc = myList[2:5]
print(slc)

#step
#third entry is step
stslc = myList[1:4:2]
print(stslc)

#quick trick to rever a list
rev = myList[::-1]
print(rev)

#copying list so that original does not change when the copy is modified
#1
list_cpy  = myList.copy()
list_cpy.append("Hello")
print(list_cpy)
print(myList)

#2 
list_cpy  = list(myList)
list_cpy.append("Hi")
print(list_cpy)
print(myList)

#3
list_cpy  = myList[:]
list_cpy.append("H")
print(list_cpy)
print(myList)


#list comprehention
list_simple = [1,2,3,4,5]

#list comprehension is mdifying elements using just oone line

list_sq = [i*i for i in list_simple]
print(list_sq)






