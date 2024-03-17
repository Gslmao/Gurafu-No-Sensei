import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

x = sy.symbols('x')

MathFunc = {
    'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
    'cosec': lambda x: 1/np.sin(x), 'sec': lambda x: 1/np.cos(x), 'cot': lambda x: 1/np.tan(x),
    'log': np.log
}

func_str = input('Enter the function: ')

# Extract the expression from the user input
ExpList = func_str.split("=")
if len(ExpList) == 2:
    expression = ExpList[1]
else:
    expression = func_str

# Parse and simplify the expression
func = sy.simplify(expression)

# Define the x values
x_val = np.linspace(-100, 100, 10000)

# Use NumPy vectorized operations to evaluate the function for each x value
y_val = np.vectorize(lambda val: func.subs(x, val))(x_val)

# Calculate the derivative using NumPy's np.gradient
deriv = np.gradient(y_val, x_val)

plt.plot(x_val, y_val, label=f'{expression}')
plt.plot(x_val, deriv, label='Derivative')
plt.legend()
plt.grid()
plt.show()
