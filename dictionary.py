#Dictionaries: Key-Value pairs, Unrdered, Mutable

mydict = {
    "name":"max",
    "age": 28,
    "city":"New York"
}

#accesing the key : 
value = mydict["name"]
print(value)

#add new value 
mydict["email"] = "abc@gmail.com"
print(mydict)

#delete
# mydict.pop("key") 
# mydict.pop("name")
# print(mydict)

#checking if key is present
if "name" in mydict:
    print("yes")

#iterate keys
for key in mydict:
    print(key)

#iterate values 
for value in mydict.values():
    print(value)

#iterate bth keys and values
for key, value in mydict.items():
    print(key)
    print(value)


#copy dictionary
mydict2 = mydict.copy()
mydict2["number"] = 4

print(mydict2.keys())
print(mydict.keys())

#merge tw dict
mydict.update(mydict2)
print(mydict)

#you can use any immutable element as key
# string number and tuples
my_dict = {3:9, 6:36, (1,2,3):"Hello"}
print(my_dict[(1,2,3)])








