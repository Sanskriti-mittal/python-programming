N=int(input())
for value1 in range(1,2*N):
    if value1<=N:
        print(" "*(N-value1)+"* "*(value1))
    else:
        print(" "*(value1-N)+"* "*(2*N-value1))