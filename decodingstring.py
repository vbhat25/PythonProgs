def decoded_str(encoded_string):
    parts = encoded_string.split("0")
    parts = [part for part in parts if part]
    first_name = parts[0]
    last_name = parts[1]
    ID = parts[2]
    dictn = {"First Name" : first_name, "Last Name" : last_name, "ID" : ID}
    return dictn

strng = str(input("Please enter the encoded string: "))
output = decoded_str(strng)
print(output)