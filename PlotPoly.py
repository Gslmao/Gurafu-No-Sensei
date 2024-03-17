import numpy as np
import matplotlib.pyplot as plt

def func_plot(eqn, c):
    Derv = False
    eqn = eqn.replace("^", "**")
    x_val = np.linspace(-100, 100, 4000)
    if c == 2:
        Derv = True

    try:
        exec(f"f = lambda x:{eqn.split('=')[1]}", globals())
        y_val = [f(x) for x in x_val]

        plt.plot(x_val, y_val, label=eqn)

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
        plt.grid()
        plt.axvline(0, color="black")
        plt.axhline(0, color="black")
        plt.legend()
        plt.show()
        print("Here you go")

    except Exception as ex:
        print(f"Error!! : {ex}")
