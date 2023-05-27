# constraints = ["-1x1 + -1x2 < -1","-2x1 + -3x2 < -2"]
# z           = "-3x1 + -1x2"
 

# 1 2 3 4
# 


# 0 2 2 1
# 4 6 8 6
# 6 8 10

l = [1 ,3 ,4 ,1]
print(l,l.index(min(l)))


a = [1,1,2,3,0,0,0]
A_min = min(a)

A_min_indices = [index1 for index1, element1 in enumerate(a) if element1 == A_min]

if(len(A_min_indices)==1):
    print(a.index(A_min))
else:
    print(A_min_indices)
    print(a.index(A_min))