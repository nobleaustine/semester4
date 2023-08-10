# required libraries
from sympy import *

def intial_range():

  last1 = 0
  last2 = 0
  check = False

  while(check == False):

    if((f(last1) < 0 and f(last1 + 1) > 0) or (f(last1) > 0 and f(last1 + 1) < 0)):
        a = last1
        b = last1 + 1
        check = True
    else:
        last1 = last1 + 1

    if((f(last2) < 0 and f(last2 - 1) > 0) or (f(last2) > 0 and f(last2 - 1) < 0)):
        a = last2 -1
        b = last2 
        check = True
    else:
        last2 = last2 -1 

  return a,b

def false_position_method():

    # intial range within which x for f(x) = 0 lies
    global a
    global b
    count = 0
    
    # intial error and value of the function
    calc_e = 1    
    value  = f(a)
    
    # repeat untill error is less than required
    while calc_e != 0 :

        count = count + 1
        pos = (a*f(b) - b*f(a))/(f(b)-f(a))
        pos = round(pos,rd)
        print("Iteration No. : ",count)
        print(" ")
        print("   a = ",a)
        print("   x = ",pos)
        print("   b = ",b)

        
        if f(pos) > 0 :  # updating a and b
            b = pos
        else :
            a = pos

        calc_e = abs(value - f(pos)) # calculating error
        calc_e = round(calc_e,rd)
        value  = f(pos)              # storing value at this point for error calculation
        
        print(" ")
        print("   error = ",calc_e)
        print(" ")
        
    print("ans : ",pos)

func = str(input("enter function : "))

rd   = int(input("accuracy : "))
func = "lambda x : " + func
f = eval(func)
x = symbols('x')
f_ = eval("lambda x :"+str(f(x).diff(x)))

a,b = intial_range()
false_position_method()





