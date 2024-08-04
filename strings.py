# Strings : ordered, immutable, text representaton
from timeit import default_timer as timer
mystr = "hello world"

#multiline string

mult_str = """
Hello how are you?
I am good
"""
print(mult_str)

#slicing 
substring  = mystr[1:5]
print(substring)

#reversing 
rev = mystr[::-1]
print(rev)

#concat 
add_s = mystr + "what a day!"
print(add_s)

#iterate:
greeting = "hello"
for i in greeting:
    print(i)

#checking fr sub
if "wor" in mystr:
    print("yes")

#trimming white space 
mystring = '  Hello   '
print(mystring)
print(mystring.strip())

#upper case 
print(mystring.upper())

#find sub string 
mystr = "Hello world! What a day"
location_of_day = mystr.find("day")
print(location_of_day)

#count occurence of a substring
count = mystr.count("l")
print(count)

#replace 
new_str = mystr.replace("world", "univers")
print(new_str)

#convert list to string
mylist = mystr.split()
print(mylist)

#splitting all characters of string
# mylist = [*mystr]
# print(mylist)

#join 
my_new = "-".join(mylist)
print(my_new)


# iterating over a list and adding to a string
#is very time consuming.

# bad code

start = timer()
mystring = ''
for i in mylist:
    mystring += i
# print(mystring)
stop = timer()
print(stop-start)


#good
start = timer()
mystring = ''.join(mylist)
# print(mystring)
stop = timer()
print(stop-start)

#formatting

#old
var = "Tom"
my_string = "this variable is %s" % var
print(my_string)

#old2
var = "Tom"
age = 28
mystr = "the variable is {} and age is {}".format(var, age)
print(mystr)

#since python 3.6 you can use
#f string
mystr = f"this is {var} var age is {age}"
print(mystr)








