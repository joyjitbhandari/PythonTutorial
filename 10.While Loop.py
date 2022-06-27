#there are while and for loop
# while loop
i = 1
while i<=7 :
    print(i)
    i += 1
print('\n')

# break statement is use for break or stop the loop
i = 1
while i < 7:
    print(i)
    if i == 3:
       break
    i += 1
print('\n')

# with continue statement we can stop current iteration
i = 0
while i <7:
    i+=1
    if i == 2:
        continue
    print(i)