a_str = input()

letter = ""
for letter in a_str:
    if letter.isupper():
        print(letter.lower(), end="")
    else:
        print(letter.upper(), end="")
