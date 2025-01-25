def find_square(start, end):
    Square = []
    for i in range(start, end + 1):
        if (i ** 0.5).is_integer():  # Check if the square root is an integer
            Square.append(i)
    print(*Square)

# Collecting user input
start = int(input('Enter the start point: '))
end = int(input('Enter the end point: '))

# Calling the function
find_square(start, end)
