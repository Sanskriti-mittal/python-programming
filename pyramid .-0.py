N=int(input())
for row in range(N):
    print(". "*(N-1-row)+"0 "*(2*row+1)+". "*(N-1-row))