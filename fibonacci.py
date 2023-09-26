def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

num = int(input("Enter the number : "))

if num <=0:
    print("Enter positive integer")
else:
    for i in range(num):
        print(fibonacci(i))