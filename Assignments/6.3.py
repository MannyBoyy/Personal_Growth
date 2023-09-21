num = float(input())
float = "{0:.2f}".format(num)

str_num = str(float)

spaces = " " * (12 - len(str_num))




print(spaces + str_num)