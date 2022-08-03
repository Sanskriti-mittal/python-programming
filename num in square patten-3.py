a= int(input())
k=0
for i in range(1, a+1):
    pattern= ""
    for v in range(1, a+1):
        pattern= pattern +str(v+a*k) + " "
    print(pattern)
    k=k+1
        