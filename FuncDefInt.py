import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
from math import *

def Integration(eqnO):
    eqn = eqnO.replace("^", "**")
    exec(f'f = lambda x :{eqn.split("=")[1]}', globals())

    lim_upper = 0
    lim_lower = 0

    print("""What Type of Integration?
         1. Definite
        2. Indefinite""")
    c = int(input("Enter Number of choice"))
    if c == 1:
        lim_upper = float(input("Upper Limit"))
        lim_lower = float(input("Lower Limit"))

    x = sy.symbols('x')
    if lim_lower > lim_upper:
        print("Lower Limit cannot be greater than Upper Limit!!")
    else:
        if lim_upper == 0:
            x_coord = np.linspace(-100, 100, 10000)
            integral = sy.integrate(f(x), x)
            EqnInt = str(integral).replace("**", "^")

            print(f'The Integral of {eqnO} is {EqnInt}')
        else:
            integral = sy.integrate(f(x), x)
            IntVal = sy.integrate(f(x), (x, lim_lower, lim_upper))

            print("Value of the integral is", IntVal)
            if abs(lim_lower) < abs(lim_upper):
                x_coord = np.linspace(-abs(lim_upper) * 1.1, abs(lim_upper) * 1.1, 100000)
            else:
                x_coord = np.linspace(-abs(lim_lower) * 1.1, abs(lim_lower) * 1.1, 100000)
            ar_x = np.linspace(lim_lower, lim_upper)
            ar_y = [f(val) for val in ar_x]

        y_coord = [f(val) for val in x_coord]

        exec(f"g = lambda x: {integral}")
        IntSim = sy.simplify(integral)
        int_y = []
        for i in x_coord:
            y = IntSim.subs(x, i)
            int_y.append(y)

        integral = str(integral).replace("**", "^")
        fx = str(f(x)).replace("**", "^")

        plt.plot(x_coord, y_coord, label=f'{fx}')
        plt.plot(x_coord, int_y, label=f'{integral}')
        if lim_upper != 0:
            plt.fill_between(ar_x, ar_y, color='green', alpha=0.3)

        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.legend()
        plt.grid()
        plt.show()

