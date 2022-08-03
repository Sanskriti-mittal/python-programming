N=int(input())
counter=1
for i in range(1, N+1):
    row=""
    for j in range(1, i+1):
        row=row+str(counter)+" "
        counter=counter+1
    print(row)
    