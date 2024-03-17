print("GURAFU NO SENSEI")

mFunc = ["sin", "cos", "tan", "cosec", "sec", "cot", "log"]
Equation = input("Enter Your equation")

for i in mFunc:
    if i in Equation:
        SpFunc = 'true'
    else:
        Poly = 'true'
print(SpFunc)
