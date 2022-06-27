def fibonacci(n):
    if n < 0:
        print("incorrect value ")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print('Enter the fibonacci value ')
n = int(input())
if n > 0:
    F = fibonacci(n)
    print(F)
else:
    print('Enter the correct value')
