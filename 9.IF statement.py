# now talk about conditional statements  that is if
#only if else statement
a = 23
b =100
if b>a :
    print('b greater than a\n')
else: print('a is greater\n')

# now elif statement
a= 10
b =20
c =30
if a>b>c:
    print('a is greater\n')
elif b>a>c:
    print('b is greater\n')
else: print('c is greater\n')

#shorthand if else statement
a= 100
b =25
print('a is greater than b') if a>b else print('equal') if a==b else print('a  is smaller than b')