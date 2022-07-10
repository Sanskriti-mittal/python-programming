N=int(input())
sum_of_factor=0
for factor in range(1,N+1):
    if N%factor==0:
        sum_of_factor=sum_of_factor+factor
print(sum_of_factor)