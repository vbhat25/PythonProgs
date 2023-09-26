def reversed_integer(number):
    return int(str(number)[::-1])

input = int(input("Enter a number: "))
output = reversed_integer(input)
print("The reversed integer is : ",output)