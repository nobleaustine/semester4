
from sympy import *

func = str(input("enter function : "))
func = "lambda x :" + func
f = eval(func)
x = symbols("x")
y = eval("lambda x :"+str(f(x).diff(x)))
print(str(f(x).diff(x)))
print(y(0)) 

K = True
while(K==True):
    m = float(input("f of "))
    print(round(f(m)))
    print(round(y(m)))
    K = bool(input("continue or not : "))


