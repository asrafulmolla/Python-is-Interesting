def find_divisor(number):
    number = abs(number)
    divisor = []
    for i in range(1, number +1):
        if number %i==0:
            divisor.append(i)
    return divisor

num = int (input ('Enter a Number: '))
divisor= find_divisor(num)
print (divisor)