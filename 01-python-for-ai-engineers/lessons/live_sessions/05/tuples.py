# tuples
from tkinter import YES
from typing import Literal


points = (3,4)
person = ("Sam",99,"Nigeria")
emoty_tuple = ()


#anotehr method of definig tuple
a = 3,4
print (a)
print(type(a))

# one item tuple
x = (5,)
print(type(x))


## Tuples are orderd

print(a[0])

numbers = (3,4,5,6,7,8,9,10)
print(numbers[-1])

print(numbers[1:3])


# Tuples are immutable

some_list = [12,3,4]
some_list[0] = 14
print(some_list)

some_tuple = 12,3,4
# some_tuple[0] = 14

###  cover to lsit , make chnages then back to tuple or wor with existing tuples and create new ones from it

points_list = list(points)
print(type(points_list))
points_list[1] = 5
points_list_tuples = tuple(points_list)
print(points_list_tuples)
# print(points_list)

new_tuples = (points[0],5)

print(new_tuples)

### Inbuilt Tuple methodds: count and index

votes = ("yes","yes","no","no","yes")

yes_counts = votes.count("yes")
no_counts = votes.count("no")

print(f"YES COUNTS: {yes_counts} and No counts {no_counts}")
# index gives us first postion of the slement in question


yes_index = votes.index("yes")
print(yes_index)


## Unapcking Tuples


person  = ("John","Nigeria",67)

name , country, age = person

print(name)
print(country)
print(age)



#collect the rest with *

scores =(20,30,40,60,20)

first , *rest = scores

print(first)
print(rest)


# Ingroing wiht underscore


person  = ("John","Nigeria",67)

name , *_ = person
print(name)



#convrting betwen lists and tuples
list1 = [1,2,4,5,5]
tuple1 = tuple(list1)