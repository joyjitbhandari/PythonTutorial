# Python is object oriented programming language
# where everything is defined in an object
#Now creating a class
class myclass:
    x =3
    #print(x)
p1 = myclass()
print(p1.x)

# class have function with init keyword
class person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def myfunction(self):
        print('Hi '+ self.name)
p2 = person("Tony", 32)
p2.myfunction()
print(p2.name) # its returns the class value name
print(p2.age)