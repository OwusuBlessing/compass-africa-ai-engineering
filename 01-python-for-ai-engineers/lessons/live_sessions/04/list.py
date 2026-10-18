# LIST stores mnay values in order (mutable compared to string)





names = ["Sam","Jack","Joe"]

scores = [50,90,45,True,"SAM"]

empty = []


#

messages = ["tell me about ai", "summarize docs"]

docs = ["doc1.txt","doc2.txt","doc3.txt"]

results = []


## LISTS ARE ORDERED

names = ["Sam","Jack","Joe"]
print(f"Previous id : {id(names)}")
#  SAM  --> 0
#  JACK --> 1
#  JOE --> 2

print(names[0])


## LIST ARE MUTABld

names[0] = "GIG"
print(f"NEW  id : {id(names)}")

### memebrs slicing lenght applies similary to strings

## ADDING ITEMS

names.append("SAMSON") # just a single item
print(names)

new_names = ["BOLA","David"]
 
names.extend(new_names) # add multiple items

print(names)


#Joining multipe lists
a = [1,2]
b = [3,4]

c  = a + b
print(c)

##remove itesm

# names.remove("Samson")

#Removing by index
last = names.pop() #remove last eleemnton the lsit
second = names.pop(1) # remove element on index 1
print(last)
print(second)


# Find, count, sort , reverse

scores = [45,60,90]
print(scores.index(90))

#sort thing
scores = [90,67,100]
scores.sort(reverse=True)
print(scores)

## sort sorted
new_scores = [3,1,5]
latest_scores = sorted(new_scores)

## reverse
new_scores.reverse(  
)

# when deaing wiht numbers

numbers = [4,6,1,9]

print(max(numbers))
print(min(numbers))
print(sum(numbers))


# copy
a = [1,2,3,4]
b = a.copy()

names ="Sam,Jack,Fred"
names_list = names.split(",")
print(names_list)

for i in names:
    print(i)