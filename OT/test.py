import re
variable = "x1"
txt = "-9.44x1 + 7x2 + 9x3 -3s1 -7x5 -7.9x7"
x = re.search(r"[-]?\d+[.]\d+"+f'{variable}'+"|[-]?\d+"+f'{variable}', txt)

print(txt)
print(x.match())
# print(str(x[0]))
constraints=["2x1 + 1x2 + 1s1 = 50","2x1 + 5x2 + 1s2 = 100","2x1 + 3x2 + 1s3 = 90"]
variables = ['x1','x2','s1','s2','s3']

table = []
finalConstraints = []

for constraint in constraints:

    coefficient = []
    equation = "CUT"

    for variable in variables:

        extractedValue =[]
        extractedCoefficient = []

        if(constraint.find(variable) !=-1):
            extractedValue = re.search(r"[-]?\d+[.]\d+"+f'{variable}'+"|[-]?\d+"+f'{variable}',constraint )
            equation = equation + " + " + str(extractedValue[0])

            extractedCoefficient = re.search(r"[-]?\d+[.]\d+|[-]?\d+",str(extractedValue[0]) )
            coefficient.append(int(extractedCoefficient[0]))

        else:
            equation = equation + " + " + f'0{variable}'
            coefficient.append(0)

    equation = equation[6:len(equation)]

    finalConstraints.append(equation)
    table.append(coefficient)

print(table)
print(finalConstraints)