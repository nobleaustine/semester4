# importing required libraries
import re  
   
# required global variables
# func       = [] # to store function parameters
# polynomial = '' # user input polynomial

# a = 0
# b = 0
# required functions
# a0x^0 + a1x^1 + a2x^2 + a3x^3 + .... + aix^i + ... + anx^n
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

def fofx(x):
    global func

    value = 0 # for getting value of function at x
    for term in func:
        value = value + term[0]*(x**term[1]) # contribution of each term
    return value

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

def print_ans(polynomial,ans):
    print(f'The solution of the equation {polynomial} = 0 is {str(ans)}')



