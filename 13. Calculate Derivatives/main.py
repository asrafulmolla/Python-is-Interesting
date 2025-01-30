import sympy as sym

# Define the symbol
x = sym.Symbol('x')

# Get the function from the user
func_input = input("Enter the function: ")

# Parse the input string into a SymPy expression
func = sym.sympify(func_input)

# Compute the derivative
derivative = sym.Derivative(func, x).doit()

# Print the result
print("The derivative of", func, "with respect to x is:", derivative) 