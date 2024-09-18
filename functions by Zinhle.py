# function that calculates the sum of all numbers from 1 to n and returns the value
n = int(input("please enter the nth number: "))
def sum_number (n):
    for i in range(n+1):
        sum = i + n 
    return sum
that = sum_number(n)
print("The sum is:", that)