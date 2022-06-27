# dictionaries are define as {} braces , its key value pair

mydiction= {
    "name" : "joyjit",# its key-value pair
    "age" : 5,
    "country": "India",
    "email" : "er.joyjit.bhandari@gmail.com"
}

print(mydiction)
print(mydiction["name"])  # its prints the name keys value

#changing specific item value by its key name
mydiction["age"] = 21
print(mydiction)

#printing all key names by one by one
for i in mydiction:
    print(i)
print('\n')

#printing all values by one by one
for i in mydiction:
    print(mydiction[i])
print('\n')

# another method for seeing the values
for i in mydiction.values():
    print(i)
print('\n')

# for printing all key and values by looping
for i,j in mydiction.items():
    print(i,j)
print('\n')

print(len(mydiction))

# to add key value in dictionary
mydiction["job"]= "Engineer"
print(mydiction)

# to remove items is dictionary by specific
mydiction.pop("age")
print(mydiction)

# remove from last
mydiction.popitem()
print(mydiction)
del mydiction["name"]
print(mydiction)

mydiction.clear()
print(mydiction)
