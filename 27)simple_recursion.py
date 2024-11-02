# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1) + fib(n-2)
# This is a example of the famous fibiyachi series


def list_recursion(elements):
    total = 0
    for element in elements:
       
        if type(element) == type([]):
            total+= list_recursion(element)
        else:
            total += element

    return total

# print(list_recursion([1, 2, [3, 4], [5, 6]]))

def recursion(number):
    if number <0:
        return 'dude this is a negative number'
    else:
        if number ==1 or number == 0:
            return 1
        return number * recursion(number - 1)

# print(recursion(5))

# def sum_of_digits(numbers):
#     total = 0
#     if numbers < 0:
#         return 'Need to have a positive number'
#     else:
#         for i in range(len(str(numbers))):
#          total += int(str(numbers)[i])

#         return total
         
def sum_of_digits(numbers):
    if numbers < 0:
        return 'Need to have a positive number'
    else:
        if len(str(numbers)) == 1:
            return numbers
        return int(str(numbers)[0]) + sum_of_digits(int(str(numbers)[1:]))
        

# print(sum_of_digits(345))

def sumDigits(n):
    # Check if 'n' is 0 (base case for summing digits)
    if n == 0:
        # If 'n' is 0, return 0 (no digits to sum)
        return 0
    else:
        # If 'n' is not 0, calculate the sum of the last digit (n % 10) and
        # recursively call the sumDigits function on the remaining digits (n / 10)
        return n % 10 + sumDigits(int(n / 10))

# Print the result of calling the sumDigits function with the input value 345
# print(sumDigits(345))

def sum_series(number):
     if number <=0:
         return 0
     return number + sum_series(number-2)

# print(sum_series(7))


def harmonic_sum(number):
    if number <=1:
        return 1
    return 1/number + harmonic_sum(number -1)

print(harmonic_sum(1))




