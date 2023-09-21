num_int = int(input())  # Do not change this line
# we start by adding the input nbumber into this statement. 

allnum = [] # 
# then we create a list that can contain all the numbers that the loops outputs.

while num_int >= 0 and num_int <= 10000:
    allnum.append(num_int)
    num_int = int(input())
#In this algorithim we have used a while loop determine that the number that the user inputs is a valid range.
#then we add the number that the user input to a list called allnum that contains all the number that has been inputed

max_int = max(allnum)
#then we can determine the max number by adding the max of the allnum into this variable.

print(max_int)
#and then we simply print out  the variable that contains the max number. 



#print(max_int)  # Do not change this line


#i = 0
#allnum = []
#if num_int > 0: 
#    for i in range(100):
#        allnum.append(num_int)
#        if num_int > 0:
#            num_int = int(input())
#
#print (i, allnum)