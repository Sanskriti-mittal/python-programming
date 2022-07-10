N=int(input())

for value in range(1,N+2):
    if value==1:
        print("-"*(N+1))
    elif value==N:
        print("|/")
    else:
        print("|"+ +"/"+"")