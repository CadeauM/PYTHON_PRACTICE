def FizzBuzz(n):
    if n % 5 == 0:  # the number is divisible by 5
        return "Fizz"
    elif n% 3 == 0:  # the number is divisible by 3
        return "Buzz"
    else:
        return n  # if the number is not divisible by any the number is returned.
        
print(f"Your answer is:", FizzBuzz(10))
