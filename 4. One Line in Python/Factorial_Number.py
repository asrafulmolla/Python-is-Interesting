n = int(input('Enter a number: '))
fact = lambda n: 1 if n <= 1 else n * fact(n-1)
print(f"Factorial of {n} is {fact(n)}")
