
from tabulate import tabulate
import numpy as np

# print(" ")
# print("----------------------------------------------------------------- ")
# print(" ")
# print("User Inputs :")
# print(" ")

# no_jobs = int(input("Enter the total number of jobs : "))
# print(" ")
# jobs = [f'J{i}' for i in range(no_jobs)]

# print("Enter the time of processing the jobs in the")
# print("increasing order of job label ike,")
# print("J0, J1, J2, ...., Jn for each machine A and B ")
# print(" ")

# machine_A = [int(x) for x in input('          A : ').split()]
# machine_B = [int(y) for y in input('          B : ').split()]
# table = [machine_A, machine_B]
# table = np.array(table)

jobs  = ["J1","J2","J3","J4","J5","J6","J7","J8","J9"]
table = [[2,5,4,9,6,8,7,5,4],[6,8,7,4,3,9,3,8,11]]
# table = [[2,4,5,7,1],[3,6,1,4,8]]

print(" ")
print("----------------------------------------------------------------- ")
print(" ")
print("                  SEQUENCING TABLE ")


def display_table(jobs,table):

    head     = ["machines\jobs"] + jobs
    view_table =[ ["A"] + table[0]]
    view_table.append(["B"] + table[1])
    

    print(tabulate(view_table,headers=head,tablefmt="grid"))
    print(" ")

def algorithm(jobs,table):

    machine_A = {}
    machine_B = {}
    A_jobs    = []
    B_jobs    = []
    count     = 0
    
    for pos,job in enumerate(jobs):
        machine_A[job] = table[0][pos]
        machine_B[job] = table[1][pos]

    # machine_A = dict(sorted( machine_A.items(), key=lambda item: item[1]))
    # machine_B = dict(sorted( machine_B.items(), key=lambda item: item[1]))
    
    
    while(len(machine_A) !=0):

        count = count + 1
        A_min = min(machine_A.values())
        B_min = min(machine_B.values())

        
        A_min_jobs = [key for key, value in machine_A.items() if value == A_min]

        B_min_jobs = [k for k, v in machine_B.items() if v == B_min]

        if(A_min<B_min):
            if(len(A_min_jobs) == 1):
                A_jobs.append(A_min_jobs[0])
                del machine_A[A_min_jobs[0]]
                del machine_B[A_min_jobs[0]]
            else:
                B_new = [value for key, value in machine_A.items() if key in B_min_jobs]
                B_new.sort()
                B_new.reverse()
                B_min_jobs = []
                for b in B_new:
                    B_min_jobs.append(list(machine_A.keys())[list(machine_A.values()).index(b)])
                for i in range(len(B_min_jobs)):
                    B_jobs.append(B_min_jobs[i])
                    del machine_A[B_min_jobs[i]]
                    del machine_B[B_min_jobs[i]]
                    
                

        elif(B_min<A_min):
            if(len(B_min_jobs) == 1):
                B_jobs.append(B_min_jobs[0])
                del machine_B[B_min_jobs[0]]
                del machine_A[B_min_jobs[0]]
            else:
                B_new = [value for key, value in machine_A.items() if key in B_min_jobs]
                B_new.sort()
                B_new.reverse()
                B_min_jobs = []
                for b in B_new:
                    B_min_jobs.append(list(machine_A.keys())[list(machine_A.values()).index(b)])
                for i in range(len(B_min_jobs)):
                    B_jobs.append(B_min_jobs[i])
                    del machine_A[B_min_jobs[i]]
                    del machine_B[B_min_jobs[i]]
                

        else:
            A_jobs.append(A_min_jobs[0])
            B_jobs.append(B_min_jobs[0])

            del machine_A[A_min_jobs[0]]
            del machine_B[A_min_jobs[0]]
            del machine_B[B_min_jobs[0]]
            del machine_A[B_min_jobs[0]]

        print("Iteration : ",count)
        print("Machine A : ",A_jobs)
        print("Machine B : ",B_jobs)
        print(" ")

    B_jobs.reverse()

    sequence = A_jobs + B_jobs

    print(" ")
    print("Optimal Sequence : ",sequence)
    print(" ")

display_table(jobs,table)
algorithm(jobs,table)




