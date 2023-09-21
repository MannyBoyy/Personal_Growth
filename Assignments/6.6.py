name = input()

full = name.split()

last_name = full[0]
first_name = full[-1]
initial = first_name[0]
 

init = initial.upper()
last= last_name.capitalize()
full_name= init+". "+ last[:-1]


print(full_name) 