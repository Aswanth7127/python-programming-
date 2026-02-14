text = input("Enter a string: ")
if len(text) == 0:
    print("String is empty.")
else:
    first = text[0]
    last = text[-1]
    index = len(text) // 2
    middle = text[index]
    print("First character:", first)
    print("Last character:", last)
    print("Middle character:", middle)
