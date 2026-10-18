# 

from re import M, U
from telnetlib import EL
from tkinter import E


text ='Bola said she "AI IS DEAD" '

##indexing

some_string = "SAMUEL"
#  S - 0
#  A
#  M
#  U
#  E
#  L -5


print(some_string[0])

## SLICING

# start - end + 1

print(some_string[0:3])

## REVERSE
print(some_string[::-1])


## Length and members

text = "python"
print(len(text))

print("SA" in text)
print("Py" in text)


## cocncetaiontion

first = "AI"
second = "Engineer"

print(first + " " +  second)


## string methods

name = "ENGINEER"
print(name.lower())

