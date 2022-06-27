# a function is defined by "def" keyword and its passes gthe parameters then exicute conditions and return the expecten value or result
def my_fun():
    print("Hi, Python!")

my_fun() # where calling the function

# function with parameter
def my_name(name):
    print('Hi!'+name)
#print('enter your name')
#name=input()
#my_name(name)
my_name("joy")

# using return statement
def my_newfun(x):
    return 5*x
print(my_newfun(5))
print(my_newfun(2))
print(my_newfun(10))