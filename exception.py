# for exception try and except block is here
# if try got error then except message will print
try:
    print(x)
except:
    print("exception generate\n")

# multiple error message printing
try:
    print(x)
except NameError:
    print("x is not defind\n")
except:
    print("something else is wrong\n")

# try except and else method to catch error
try:
    print("Hii")
except:
    print("Something is wrong\n")
else: # for printing non error message
    print("Nothing will wrong\n")


# try,except and finally method for printing message
try:
    print("Hii there")
except:
    print("Something is wrong\n")
finally: # for printing non error message
    print("Process complete")
