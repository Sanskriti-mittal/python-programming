N=int(input())
for i in range(N-1):
    strign=""
    for j in range(1, i+1):
        strign=" "*(2*j-1)+str(i+1)
    print("1"+strign)
last_row=""
for k in range(1,N+1):
    last_row=last_row+str(k)+" "
print(last_row)