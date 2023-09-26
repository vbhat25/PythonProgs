def decimal_to_octal(decimal_number):
    return oct(decimal_number)

input = int(input("Enter a decimal number: "))
output = decimal_to_octal(input)
print ("The octal number for the decimal number", input, "is", output.replace("0o",""))