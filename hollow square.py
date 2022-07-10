N=int(input())
for value in range(1,N+1):
    if value == 1 or value == N:
        print("* "*N)
    else: 
        print("* "+"  "*(N-2)+"*")