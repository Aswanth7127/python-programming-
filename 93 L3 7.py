text = input("Enter a string: ")
l = text.lower()
length = len(text)
vowel_count = 0
consonant_count = 0
vowels = "aeiou"
for i in l:
    if i.isalpha():  
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Total length of string:", length)
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
