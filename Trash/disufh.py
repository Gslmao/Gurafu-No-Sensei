import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

eqn = input("Enter your Trigonometric Equation with x an y on either sides of equality")
eqn = eqn.replace("^", "**")
exec(f'f = lambda x :{eqn.split("=")[1]}', globals())

def DefInt():
    lim_upper = float(input("Upper Limit"))
    lim_lower = float(input("Lower Limit"))

    x = sy.symbols('x')

    x_coord = np.linspace(lim_lower+10 , lim_upper+10, 1000)
    y_coord = [f(rhs) for rhs in x]

    IntVal = sy.integrate(f(x), (x, lim_lower, lim_upper))
    integral = sy.integrate(f(x), x)

    print("Value of the integral is", IntVal)

    g = lambda x: sy.simplify(integral).subs('x', x)
    int_y = [g(val) for val in x_coord]

    plt.plot(x, y_coord, label = f'{f}')
    plt.plot(x_coord, int_y, label = f'{integral}')

    plt.fill_between(, lim_upper, where=[(lim_lower <= val <= lim_upper) for val in x_coord], color = 'green', alpha = 0.5)
    plt.show()

#print("""What Integration
 #   1. Defenite
 #   2. Indefenite""")

DefInt()
#plt.plot(x,f(x))
#plt.axhline(color = 'black')
#plt.axvline(color = 'black')
#plt.show()