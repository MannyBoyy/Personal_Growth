stop_range = int(input())
num_devisors = int(input())


def sum_of_2_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum
#using def will basically add another function to find ceratin calculations.
def divisors(number):
    divisors = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisors += 1
    return divisors

#Focus on first part trying to plus two numbers together and seeing if that number  equals to it self.
for number in range(10, stop_range):
    sum = sum_of_2_digits(number)
    if sum ** 2 == number:
        print(number)
        #this is then the second part of the loop that reveals the numbers with the positive divisors.

for number in range(1, stop_range):
    if divisors(number) == num_devisors:
        print(number)
#good to separate both of the calculations because then it would calc the second one without it stopping completely.
#note this gave me a big brain fart


                    