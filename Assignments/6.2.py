a_str = input()  # Do not change this line

# Complete the program below
odd = ""

for letter in range(len(a_str)):
        if letter % 2 == 0:
                
            odd += a_str[letter]
        
print(odd)
