import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

x = sy.symbols('x')

def SpcPlot(uInput,c):
    try:
        Derv = False
        if c == 2:
            Derv = True

        uInput = uInput.replace("^", "**")
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
            y = ExpSim.subs(x, i)
            y_val.append(y)

        plt.plot(x_val, y_val, label=f'{ExpSim}')

        if Derv:
            deriv = []
            for i in range(len(x_val) - 1):
                dx = x_val[i + 1] - x_val[i]
                dy = y_val[i + 1] - y_val[i]
                derivative = dy / dx
                deriv.append(derivative)
            deriv.append(deriv[-1])
            plt.plot(x_val, deriv, label='Derivative')
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.axvline(0, color="black")
        plt.axhline(0, color="black")
        plt.legend()
        plt.grid()
        plt.show()
        print("Here you go")
    except Exception:
        pass


