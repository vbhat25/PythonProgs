def nfibonacci(n):
    if n<=1:
        return n
    else:
        #initial values
        fibn_1 = 0
        fibn_2 = 1
        for i in range (2,n+1):
            #updating variables
            fib_n = fibn_1 + fibn_2
            fibn_1,fibn_2 = fib_n,fibn_1
        return fib_n

n = int(input("Enter value of n: "))
if n < 0:
    print("Error, Please enter positive integer")
else:
    output = nfibonacci(n)
    print("The",n,"th value in the series is : ",output)