text = input("Enter a string: ")
print("\nCharacters in Forward Order:")
i = 0
while i < len(text):
    print(text[i], end=" ")
    i += 1
print("\n\nCharacters in Reverse Order:")
j = len(text) - 1
while j >= 0:
    print(text[j], end=" ")
    j -= 1
