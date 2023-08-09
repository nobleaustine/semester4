
# required libraries
import re  
import numpy as np

a = ["1x1 + 1x2 + 1x3 = 2","x1 + 2x2 + 1x3 = 5","2x1 + 3x2 + 4x3 = 11"]

def extractCoefficients(equations):
    
    variables = []
    matrix = []
    parts  = [] # to store the parts of equation split by "+"

    for equ in equations:
        result=re.findall(r'[x]\d+', equ)
        variables.append(result)
    variables = [ x for y in variables for x in y]
    variables = list(set(variables))
    variables = sorted(variables)
    
    for i in range(len(variables)):

        coefficients=[]

        for equ in equations:

            parts = equ.split('+|-')
            parts = [y for x in parts for y in x.split(" - ")]

            for element in parts:

                if(element.find(variables[i]) !=-1):

                    if(element.find('-') !=-1):
                        result=re.findall(r"\d+", element)
                        coefficients.append(int('-'+result[0]))
                    else:
                        result=re.findall(r"\d+", element)
                        coefficients.append(int(result[0]))

        matrix.append(coefficients )
    matrix = np.transpose(matrix)
    return matrix

k = extractCoefficients(a)
print(k)
