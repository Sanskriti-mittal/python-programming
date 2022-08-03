N=int(input())

for i in range (N):
    string=""
    for j in range(1,N-i+1):
        string=string + str(j)+" "
    print(" "*(i) +string)