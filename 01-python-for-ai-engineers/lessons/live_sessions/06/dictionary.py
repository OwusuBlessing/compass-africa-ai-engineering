# Dictionayr stores key:value pairs

person = ("sam",99,"Nigeria")

person = {

"name":"Sam",
"age":99,
"Country":"Nigeria"


}

print(person)



# RedaAING VALUES

print(person["name"])
print(person["age"])
print(person["Country"])


print(person.get("name"))
print(person.get("age"))
print(person.get("Country"))


## ADING AND CHAING VALUES 
#note: keys are unique

person["email"] = "sam@gmail.com"
person["name"] = "Joe"
print(person)




## update maning at once

new_person = {"name":"Jay","age":100}

person.update(new_person)
print(person)



# ## Removing items

person.pop("name")

# name = input("Enter your name:")
# age = input("Enter your age:")

# user = {"name":name,"age":age}

# print(f"HERE IS YOUR DIDCTIONARY DATA : {user}")


# jeys values and items


print(person.keys()) 
print(person.values())
print(person.items()) # [('name',"Sam")]
