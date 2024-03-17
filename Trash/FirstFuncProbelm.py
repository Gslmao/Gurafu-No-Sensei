import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

x = sy.symbols('x')

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
    return None

MathF = MathFuncFind(uInput, func)

if MathF is not None:
    print("Matching substring found:", MathF)
else:
    pass

function = MathFunc[MathF]

print(function)

eqn = f'{uInput}'

if MathF == "log":
    x_val = np.linspace(1e-15, 100, 10000)
else:
    x_val = np.linspace(-100, 100, 10000)

y_val = []
for i in x_val:
    try:
        y_val.append(function(i))
        print(function(i))
    except (ZeroDivisionError, ValueError):
        y_val.append(np.inf)
        print(np.inf)

deriv = np.gradient(y_val, x_val)

plt.plot(x_val, y_val, label=f'{eqn}')
plt.plot(x_val, deriv, label='Derivative')
plt.legend()
plt.grid()
plt.show()
