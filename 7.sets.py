# sets , its define as {}, its is unordred

myset = {'apple','banana','cherry'}
print(myset)

for i in myset:
    print(i)

#cheaking the item is present in myset or not
print('apple' in myset)
print('lemon' in myset)

# adding item to myset
myset.add('lemon')
print(myset)
# for adding multiple items in myset
myset.update(['lemon','lichi'])
print(myset)

print(len(myset))

# to remove item from myset
myset.pop()
print(myset)
myset.remove("banana")
print(myset)

# to clear the whole set
#myset.clear()
#print(myset) its showing error because set dosenot exist after clearing the set


