#Operators are 6 types
                #Arithmetic (ex = + , _ , * , /)
                #Comparison (ex = to compare to objects and returns boolean value true or false)
                #Logical (ex = and, or , not)
                #Assignment ( use to assign values to variables)
                #Bitwise ( )
                #Conditional ( )

#Arithmetic Operators
print("Addition:",40+50)
print("Subtraction:",50-30)
print("Multiplication:",50*100)
print("Division:",50/ 2)
print("Decimal:",50//3) # prints only Decimal value not float value
print("Modulus:", 50%2) # prints the modulus value
print("Power:", 3**2) # here 2 power of 3
print('\n')

#Comparison Operators
print(2==2)
print(2==3)
print(2 == '2')
print(5>3)
print(5>=3)
print(10>12)
print(2>=3)
print('\n')

#Logical Operators
print(2==2 and 3==3)
print(2== 3 and 5==5)
print(2==2 or 3==3)
print(2==3 or 5==5)
print('\n')

#Assignment Operators
a = 2+3
print(a)
a = 5
b= 10
a += b
print(a)
print('\n')

#Conditional Operators
i = 2
print("low" if i<10 else "high")
