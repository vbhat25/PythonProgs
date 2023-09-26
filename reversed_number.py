def reverse_int(number):
    num = 0
    while number > 0:
        digit = number % 10
        num= num * 10 + digit
        number = number // 10
    return reverse_int

input = int(input("Enter a number : "))
output = reverse_int(input)
print ("The reversed number is ", output)