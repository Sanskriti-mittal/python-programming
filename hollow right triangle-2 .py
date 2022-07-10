N=int(input())
for value in range(1,N+1):
    if value==N:
        print("* "*N)
    if value==1:
        print(" "*(2*(N-1))+"*")
    if value != 1 and value!=N:
        print(" "*(2*N-2*value)+ "*"+" "*(2*value-3)+"*")