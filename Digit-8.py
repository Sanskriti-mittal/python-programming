N=int(input())
for i in range(2*N+1):
    if i==0 or i==N or i==2*N:
        print("* "*(N))
    else:
        print("* "+" "*(2*N-4)+"* ")