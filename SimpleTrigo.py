import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

x = sy.symbols('x')
MathFunc = {
    'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
    'cosec': lambda x : 1/np.sin(x), 'sec': lambda x : 1/np.cos(x), 'cot': lambda x : 1/np.tan(x),
    'log': np.log
}

func = ["sin", "cos", "tan", "cosec", "sec", "cot", "log"]

def SimpleTrigo(uInput, c):
    Derv = False
    if c == 2:
        Derv = True

    def MathFuncFind(uInput, func):
        for subStr in func:
            if subStr in uInput:
                return subStr

    MathF = MathFuncFind(uInput, func)

    if MathF is not None:
        pass
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
        if function(i) != np.inf:
            y_val.append(function(i))
        else:
            y_val.append(np.inf)

    plt.plot(x_val, y_val, label=f'{eqn}')

    if Derv:
        deriv = []
        for i in range(len(x_val) - 1):
            dx = x_val[i + 1] - x_val[i]
            dy = y_val[i + 1] - y_val[i]
            derivative = dy / dx
            deriv.append(derivative)
        deriv.append(deriv[-1])
        plt.plot(x_val, deriv, label='Derivative')

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.legend()
    plt.grid()
    plt.show()
    print("Here you Go")


