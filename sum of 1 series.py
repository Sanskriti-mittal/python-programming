N=int(input())
sum_of=0
for value in range(1,N+1):
    sum_of=sum_of+int(str("1"*value))
print(sum_of)