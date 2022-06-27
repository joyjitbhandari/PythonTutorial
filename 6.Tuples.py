# tuples is unchangable
mytuple = [ 'apple' , 'banana', 'cherry']
print(mytuple)
print(mytuple[0]) # apple
print(mytuple[2]) # cherry
mytuple.insert(2,"orrange")
print(mytuple)
mytuple.pop() # remove from last

for i in mytuple:
    print(i)

print(len(mytuple))

mytuple.remove(mytuple[1]) # remove by index
print(mytuple)