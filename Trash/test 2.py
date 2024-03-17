import math
import numpy as np
import matplotlib.pyplot as plt

TrigFunc = {
    'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
    'cosec': np.arcsin, 'sec': np.arccos, 'cot': np.arctan,
    'log' : np.log
}
uInput = input('Enter the function: ')
function = TrigFunc[uInput]
angle = (input('Enter the angle: '))

eqn = f'y = {uInput}{angle}'

if uInput == "log":
    x = np.linspace(0.000000000000001, 100, 10000)
else:
    x = np.linspace(-100, 100, 10000)
y = [function(x) for x in x]

deriv = []
for i in range(len(x)-1):
    dx = x[i+1] - x[i]
    dy = y[i+1] - y[i]
    derivative = dy/dx
    deriv.append(derivative)

#dy = np.gradient(y)
#dx = np.gradient(x)
#derivative = dy / dx

plt.plot(x, y, label=f'{eqn}')
plt.plot(x, deriv, label='Derivative')
plt.legend()
plt.grid()
plt.show()
