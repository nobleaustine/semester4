
# required libraries
import re  
   
# required functions

# function to extract coefficients and power
# a0x^0 + a1x^1 + a2x^2 + a3x^3 + .... + aix^i + ... + anx^n where
# i E (...,-3,-2,-1,0,1,2,3,...)
def function_identifier(polynomial):
    
    result = [] # result to extract ai and i as a list from the string
    func   = [] # store [ai,i] for all i in polynomial

    components = polynomial.split(" + ")  # splitting as components by " + "
    for word in components:
        if bool(re.fullmatch(r'^[-+]?\d+(\.\d+)?$',word)) == True :  # checking if it is just number x^0
            result=re.findall(r'-?\d+(?:\.\d+)?', word)
            result = [float(x) for x in result]
            result.append(float(0))
        elif bool(re.search(r".*[x]$",word)) == True :               # checking if it is number times  x^1
            result=re.findall(r'-?\d+(?:\.\d+)?', word)
            result = [float(x) for x in result]
            result.append(float(1))
        else :                                                       # for all other x^i 
            result=re.findall(r'-?\d+(?:\.\d+)?', word)
            result = [float(x) for x in result]
            if len(result) == 1:
                result.insert(0,1)
        func.append(result)                                          # adding to list func      
    return func

# function to calculate the value of the polynomial at a point
def fofx(x):

    value = 0 # for getting value of function at x
    for term in func:
        value = value + term[0]*(x**term[1]) # contribution of each term
    return value

# function to calculateintial range
def intial_range():

    number_line = [-3,-2,-1,0,1,2,3]
    a = fofx(-3) # parameters of range: (a,b)
    b = 0
    for x in number_line:
        if fofx(x) > 0 : # going to right of number line to find fofx(x) > 0
            b = x
            break
        elif fofx(x) < 0 : # else changing the limit of a 
            a = x
    return a,b

# function to perform bisection method
def bisection_method(e):

    # intial range within which x for f(x) = 0 lies
    global a
    global b
    
    # intial error and value of the function
    calc_e = 1    
    value  = fofx(a)
    
    # repeat untill error is less than required
    while calc_e > e :

        midpoint = (a + b)/2
        
        if fofx(midpoint) > 0 :  # updating a and b
            b = midpoint
        else :
            a = midpoint

        calc_e = abs(value - fofx(midpoint)) # calculating error
        value  = fofx(midpoint)              # storing value at this point for error calculation
        
    return midpoint

# default polynomial for testing f(x) = x^3 + -1x + -1
# calling required functions
print(" ")
print("     ROOTS OF NON-LINEAR EQUATION USING BISECTION METHOD")
print("  ---------------------------------------------------------")
print(" ")
polynomial = str(input("Enter the non-linear equation : "))
error      = float(input("Enter the degree of error     : "))
print(" ")
func = function_identifier(polynomial)
a,b  = intial_range()
ans  = bisection_method(error)
print(f'The root of the non-linear equation {polynomial} = 0 is {str(ans)}')
print(f'The value of the function at the root is {str(fofx(ans))}')
print(" ")
