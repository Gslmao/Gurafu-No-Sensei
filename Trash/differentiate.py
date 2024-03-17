from matplotlib import pyplot as plt
from math import *
import numpy as np
from numpy import gradient, linspace

TrigFunc = {
    'sin': np.sin, 'cos': np.cos, 'tan' : np.tan,
    'cosec': 1 / np.sin, 'sec': 1 / (np.cos), 'cot' : 1 / (np.tan)

}

def para():
    llim = int(input("Enter lower lim to plot the graph"))
    ulim = int(input("Enter upper lim to plot the graph"))
    return llim, ulim

def derivative(llim, ulim):
    lhs = linspace(llim, ulim, 99999)
    y = []

    for x in lhs:
        e = f(x)
        y.append(e)

    dy = gradient(y)
    dx = gradient(lhs)
    derivative = dy / dx

    plt.plot(lhs, y, label="Equation")
    plt.plot(lhs, derivative, label="Derivative")

    plt.legend()
    plt.grid()
    plt.show()


# -------------------------------------------------------------
eqn = input("Enter your Trigonometric Equation with x an y on either sides of equality")
eqn = eqn.replace("^", "**")
f = lambda x : eval(eqn.split("=")[1])

print("""What do you want to do to yr equation?
    1. Plot
    2. Differentiate
    3. Integrate
Type the respective number to execute""")
choice = input("Choice : ")

while True:
    if choice == "1":
        pass
    elif choice == "2":
        llim, ulim = para()
        derivative(llim, ulim)
    elif choice == "3":
        pass
    break
