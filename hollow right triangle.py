N=int(input())
for value in range(1,N+1):
    if value==1:
        print("* "*N)
    if value==N:
        print("  "*(N-1)+"*")
    if value != 1 and value!=N:
        print("  "*(value-1)+"*"+" "*(2*N-1-2*value)+"*")