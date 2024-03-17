import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')

MathFunc = {
    'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
    'cosec': lambda x: 1/np.sin(x), 'sec': lambda x: 1/np.cos(x), 'cot': lambda x: 1/np.tan(x),
    'log': np.log
}

func = ["sin", "cos", "tan", "cosec", "sec", "cot", "log"]

uInput = input('Enter the function: ')

def MathFuncFind(uInput, func):
    for subStr in func:
        if subStr in uInput:
            return subStr

MathF = MathFuncFind(uInput, func)

if MathF is not None:
    print("Matching substring found:", MathF)
else:
    pass

function = MathFunc[MathF]

print(function)

eqn = f'{uInput}'

# Extract the expression on the right side of the equal sign
expression_parts = uInput.split('=')
if len(expression_parts) == 2:
    expression = expression_parts[1]
else:
    expression = uInput

# Use sympy to parse and evaluate the expression
expr = sp.sympify(expression)
x_val = np.linspace(-100,100,10000)
y_val = np.array([sp.N(expr.subs(x, val)) for val in x_val])

# Calculate the derivative using sympy
derivative = sp.diff(expr, x)
deriv = np.array([sp.N(derivative.subs(x, val)) for val in x_val])

plt.plot(x_val, y_val, label=f'{eqn}')
plt.plot(x_val, deriv, label='Derivative')
plt.legend()
plt.grid()
plt.show()
