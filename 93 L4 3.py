text = input("Enter a string: ")
alphabets = 0
digits = 0
for i in text:
    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        digits += 1
print("Number of alphabets:", alphabets)
print("Number of digits:", digits)
