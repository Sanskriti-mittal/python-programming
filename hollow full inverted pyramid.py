N=int(input())
for i in range(N):
    if i==0:
        print("* "*N)
    elif i==N-1:
        print(" "*i+"*")
    else:
        print(" "*i+"*"+" "*(2*(N-i)-3)+"*")