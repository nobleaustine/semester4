
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

def bisection_method():
  
    global a
    global b
    count = 0
    
    calc_e = 1    
    value  = f(a)
    
    
    while calc_e != 0 :

        count = count + 1
        midpoint = (a + b)/2
        midpoint = round(midpoint,rd)
        print("Iteration No. : ",count)
        print(" ")
        print("   a = ",a)
        print("   x = ",midpoint)
        print("   b = ",b)
        
        if f(midpoint) > 0 :  # updating a and b
            b = midpoint
        else :
            a = midpoint

        calc_e = abs(value - f(midpoint)) # calculating error
        calc_e = round(calc_e,rd)
        value  = f(midpoint)              # storing value at this point for error calculation
        
        print(" ")
        print("   error = ",calc_e)
        print(" ")
        
    print("ans : ",midpoint)


func = str(input("enter function : "))


rd   = int(input("accuracy : "))
func = "lambda x : " + func
f = eval(func)
a,b = intial_range()
bisection_method()







