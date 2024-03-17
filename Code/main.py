from PlotSpcFunc import SpcPlot
from PlotPoly import func_plot
from FuncDefInt import Integration
from SimpleTrigo import SimpleTrigo

print("GURAFU NO SENSEI")
Equation = input("Enter Your equation: ")

mFunc = ["sin", "cos", "tan", "cosec", "sec", "cot", "log"]
m1Func = ["sin(x)", "cos(x)", "tan(x)", "cosec(x)", "sec(x)", "cot(x)", "log(x)"]

chck = Equation.split("=")[1]

SpFunc = False
SimTrig = False
poly = False

for i in mFunc:
    if i in chck:
        SpFunc = True
    else:
        poly = True
for i in m1Func:
    if i == chck:
        SimTrig = True
        SpFunc = False
        SpFunc = False


print('''What do you want to do?
              1. Plot the Equation
              2. Plot The Derivative
              3. Plot the Integral''')
print()
c = int(input('Enter Choice: '))

if c == 1:
    if SpFunc:
        SpcPlot(Equation, c)
    elif SimTrig:
        SimpleTrigo(Equation, c)
    else:
        func_plot(Equation, c)

elif c == 2:
    if SpFunc:
        SpcPlot(Equation, c)
    elif SimTrig:
        SimpleTrigo(Equation, c)
    else:
        func_plot(Equation, c)
elif c == 3:
    if poly:
        Integration(Equation)
