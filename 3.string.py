# strings are noted as "" or ''
x = 'Hi There!'
print(x)

# indexing
print(x[0])
print(x[5])

# printing indexes
print(x[4:8])

print(x.strip()) # to remove white space
print(x.split()) # to split string to substring
print(len(x)) # to print the length of string
print(x.lower()) # its convert the string in to lower case latter
print(x.upper()) # its convert the string in to uppercase latter
print(x.isalnum()) # checks all numeric or not and return a boolean value
print(x.isupper()) # checks all upper latter or not and return a boolean value
print(x.islower()) # checks all lower latter or not and return a boolean value
print(x.replace('i','ello')) # replace the string item

# asking user to give input

print("what is your name: ")
a = input()
print("Hello "+a)
