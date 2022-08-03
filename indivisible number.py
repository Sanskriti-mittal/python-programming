N=int(input())
number_not_divisible=0
for k in range(1,N+1):
    count=0
    for i in range(2,11):
        if k%i==0:
            count=count+1
    if count==0:
        number_not_divisible += 1
print(number_not_divisible)