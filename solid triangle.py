N=int(input())
for value in range(1,N+1):
    if value==1:
        print("* "*N)
    elif value==N:
        print(" "*(2*N-2)+"*")
    else:
        print(" "*(2*value-3)+" *"*(N-value+1))