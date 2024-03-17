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

# Define the x values
x_val = np.linspace(-100, 100, 10000)

# Extract the expression on the right side of the equal sign
expression_parts = uInput.split('=')
if len(expression_parts) == 2:
    expression = expression_parts[1]
else:
    expression = uInput

# Use sympy to parse and evaluate the expression
expr = sp.sympify(expression)

# Vectorized evaluation of the expression and its derivative
y_val = np.vectorize(lambda val: sp.N(expr.subs(x, val)) if expr.subs(x, val).is_real else np.nan)(x_val)
print(y_val)

plt.plot(x_val, y_val, label=f'{eqn}')
plt.legend()
plt.grid()
plt.show()
