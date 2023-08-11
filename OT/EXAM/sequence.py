
# jobsA  = ["J1","J2","J3","J4","J5","J6","J7","J8","J9"]
# jobsB  = ["J1","J2","J3","J4","J5","J6","J7","J8","J9"]
# A = [2,5,4,9,6,8,7,5,4]
# B = [6,8,7,4,3,9,3,8,11]

def INPUT():
    A = [float(x) for x in input("machine A time : ").split()]
    B = [float(x) for x in input("machine B time : ").split()]
    n = len(A)
    jobsA = [f'J{x+1}' for x in range(n)]
    jobsB = [f'J{x+1}' for x in range(n)]

    return A,B,jobsA,jobsB

def SORT (J1,L1,J2,L2):
    n = len(L1)
    for i in range(n):
        for j in range(i+1,n):
            if L1[j] < L1[i] :
                L1[j],L1[i] = L1[i],L1[j]
                J1[j],J1[i] = J1[i],J1[j]
            elif L1[j] == L1[i] :
                a = J1[j]
                b = J1[i]
                k = J2.index(a)
                l = J2.index(b)
                if L2[k] > L2[l]:
                    L1[j],L1[i] = L1[i],L1[j]
                    J1[j],J1[i] = J1[i],J1[j]
    
def SEQUENCING(jobsA,A,jobsB,B):

    LA = []
    LB = []

    while len(jobsA) != 0 and len(jobsB) != 0 :
        if(A[0]<B[0]):
            LA.append(jobsA[0])
            i = jobsB.index(jobsA[0])
            del jobsA[0]
            del jobsB[i]
            del A[0]
            del B[i]
        elif (A[0]>B[0]):
            LB.append(jobsB[0])
            i = jobsA.index(jobsB[0])
            del jobsB[0]
            del jobsA[i]
            del B[0]
            del A[i]
        else:
            LA.append(jobsA[0])
            i = jobsB.index(jobsA[0])
            del jobsA[0]
            del jobsB[i]
            del A[0]
            del B[i]

            LB.append(jobsB[0])
            i = jobsA.index(jobsB[0])
            del jobsB[0]
            del jobsA[i]
            del B[0]
            del A[i]
    LB.reverse()
    f = LA + LB
    return f

A,B,jobsA,jobsB = INPUT()
SORT(jobsA,A,jobsB,B)
SORT(jobsB,B,jobsA,A)
F = SEQUENCING(jobsA,A,jobsB,B)
print("optimum sequence : ",F)



