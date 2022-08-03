N=int(input())

for i in range(1,2*N+1):
    if i<=N:
        print("* "*(i)+" "*4*(N-i)+"* "*i)
    if 2*N+1>i>=N+1:
        print("* "*(2*N+1-i)+" "*(4*i-4*N-4)+"* "*(2*N+1-i))