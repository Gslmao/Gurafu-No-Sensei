import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

x = sy.symbols('x')

MathFunc = {
    'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
    'cosec': np.arcsin, 'sec': np.arccos, 'cot': np.arctan,
    'log': np.log
}

func = ["sin", "cos", "tan", "cosec", "sec", "cot", "log"]

uInput = input('Enter the function: ')

def MathFuncFind(uInput, func):
    for subStr in func:
        if subStr in uInput:
            return subStr
    return None

MathF = MathFuncFind(uInput, func)

if MathF is not None:
    print("Matching substring found:", MathF)
else:
    pass

function = MathFunc[MathF]

print(function)

eqn = f'{uInput}'

# Avoid division by zero for log function
if MathF == "log":
    x_vals = np.linspace(1e-15, 100, 10000)  # Avoid log(0)
else:
    x_vals = np.linspace(-100, 100, 10000)

y_vals = [function(x) for x in x_vals]

deriv = []
for i in range(len(x_vals)-1):  # Adjusted the loop range
    dx = x_vals[i+1] - x_vals[i]
    dy = y_vals[i+1] - y_vals[i]
    derivative = dy / dx
    deriv.append(derivative)

# Append the last derivative to make the lengths equal
deriv.append(deriv[-1])

plt.plot(x_vals, y_vals, label=f'{eqn}')
plt.plot(x_vals, deriv, label='Derivative')
plt.legend()
plt.grid()
plt.show()
