import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

x = sy.symbols('x')

#uInput = input('Enter the function: ')
def TrigPlot(uInput):
    ExpList = uInput.split("=")
    if len(ExpList) == 2:
        Exp = ExpList[1]
    else:
        Exp = uInput
    ExpSim = sy.simplify(Exp)

    if 'log' in uInput:
        x_val = np.linspace(0, 100, 10000)
    else:
        x_val = np.linspace(-100, 100, 10000)

    y_val = []
    for i in x_val:
        y = ExpSim.subs(x, i).evalf()
        y_val.append(y)

    plt.plot(x_val, y_val, label=f'{ExpSim}')
    plt.legend()
    plt.grid()
    plt.show()
