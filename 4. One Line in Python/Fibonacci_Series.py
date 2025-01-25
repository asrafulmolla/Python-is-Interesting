n=int (input('Enter a Number: '))
fib = lambda n: n if n<=1 else fib(n-1) + fib(n-2)
print (fib(n))