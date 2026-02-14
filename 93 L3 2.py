def to_lowercase(s):
    result = ""
    for i in s:
        a = ord(i)
        if 65 <= a <= 90:
            result += chr(a + 32)
        else:
            result += i
    return result
def to_uppercase(s):
    result = ""
    for i in s:
        a = ord(i)
        if 97 <= a <= 122:
            result += chr(a - 32)
        else:
            result += i
    return result
def toggle_case(s):
    result = ""
    for i in s:
        a = ord(i)
        if 65 <= a <= 90:       
            result += chr(a + 32)
        elif 97 <= a <= 122:    
            result += chr(a - 32)
        else:
            result += i
    return result
text = input("Enter a string: ")

print("Lowercase:", to_lowercase(text))
print("Uppercase:", to_uppercase(text))
print("Toggle case:", toggle_case(text))
