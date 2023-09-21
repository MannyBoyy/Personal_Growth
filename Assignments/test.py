input_string = "Hello World"
output_string = ""

for i in range(len(input_string)):
    if i % 2 == 1:
        output_string += input_string[i]

print(output_string)
