X=int(input())
N=int(input())
sum_of=0
for value in range(1,N+1):
    if value%2 != 0:
        sum_of=sum_of+X**(2*value-1)
    else:
        sum_of=sum_of-X**(2*value-1)
    
print(sum_of)