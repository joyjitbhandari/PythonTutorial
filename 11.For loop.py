# For Loop, its is can use in set,  list , tuples and more
# Printing the numbers
# range use for taking a start and end parameters
for i in range(1,5):
    print(i)
print('\n')
# range using by a increment value
for i in range(1,6,2):
    print(i)
print('\n')

# for loop using in list
fruits = ['apple','banana','cherry']
for x in fruits:
    print(x)
print('\n')

# using for loop through a string
for x in "python":
    print(x)
print('\n')

#with break statement
fruits = ['apple','banana','cherry']
for x in fruits:
    if x=='cherry':
        break
    print(x)
print('\n')

# with continue statement
fruits = ['apple','banana','cherry']
for x in fruits:
    if x=='banana':
       continue
    print(x)
print('\n')

# for using in sets
myset = {'apple','banana','cherry'}
for i in myset:
    print(i)
print('\n')

# using else keyword in for loop
# its printing the statement after completing the loop
for x in range(7):
    print(x)
else: print('Completed')