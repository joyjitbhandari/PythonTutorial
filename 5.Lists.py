#Lists are assign as [] and its changable

myList = ["apple", "banana" , "Cherry"]
print(myList)
print(myList[0])
print(myList[2])
print(len(myList))

#Replacing the mylist item
myList[1] = "orrange"
print(myList)

# printing all items one by one
for i in myList:
    print(i) # all item

#Cheaking is that item is present in my list
if "apple" in myList:
    print("yes apple in mylist")
else:print("no")

# for adding item in list use append method
myList.append("Banana") # its add at the last of the list
print(myList)

# insert by index
myList.insert(2,"Lemon")
print(myList)

# for remove item from list
myList.remove("orrange")
print(myList)

# to remove last item from list
myList.pop()
print(myList)

# deleting by index
del(myList[2])
print(myList)

# to clear whole list
myList.clear()
print(myList)






